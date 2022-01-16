from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import*
from .decorators import*

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            user.email = request.user.email
            print(user.email)
            return redirect('home')
        

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
def dashboard(request):
    jobs = Job.objects.all().order_by('-date_created')

    
    context = {'jobs':jobs}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    jobs = request.user.customer.job_set.all()

    total_jobs = jobs.count()

    context = {'jobs':jobs, 'total_jobs':total_jobs}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    print(request.user.email)
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
def createJob(request):
    jobs_list = Job.objects.order_by('date_created')
    if request.method == "POST":
        username = request.POST.get('username')
        data = request.POST
        job_form = JobForm(data)
        if job_form.is_valid():
            job = job_form.save()
            job.save()
            return redirect('home')
    job_form = JobForm()
    context = {
        "form": job_form,
        "jobs": jobs_list,
    }
    return render(request, 'accounts/job_form.html', context)



@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    form = JobForm(instance=job)
    if request.method == 'POST':

        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/job_form.html', context)


@login_required(login_url='login')
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    if request.method=="POST":
        job.delete()
        return redirect('home')

        
    context = {'item':job}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def submitProposal(request, pk):
    job = get_object_or_404(Job, id=pk)
    proposal = Proposal.objects.all()
    if request.method == "POST":
        data = request.POST
        proposal_form = ProposalForm(data)
        if proposal_form.is_valid():
            proposal_form.val = pk
            proposal = proposal_form.save()
            proposal.save()
            return redirect('home')
    proposal_form = ProposalForm()
    context = {
        "forms": proposal_form
    }
    return render(request, 'accounts/proposal.html', context)

def proposal_list(request, pk):
    proposals = Proposal.objects.all()
    jobs = Job.objects.all().order_by('-date_created')

    
    context = {'proposals':proposals, 'jobs':jobs}
    return render(request, 'accounts/apply.html', context)

