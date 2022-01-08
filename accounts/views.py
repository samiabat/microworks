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
from .filters import*
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
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

@login_required(login_url='login')
def home(request):
    jobs = Job.objects.all().order_by('-date_created')
    customers = Customer.objects.all()
    # products = Product.objects.all()

    total_customers = customers.count()

    # total_orders = orders.count()
    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()
# 'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending,
    
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
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)




# @login_required(login_url='login')
# #@allowed_users(allowed_roles=['admin'])
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    jobs = customer.job_set.all()
    job_count = jobs.count()

    myFilter = JobFilter(request.GET, queryset=jobs)
    jobs = myFilter.qs 

    context = {'customer':customer, 'jobs':jobs, 'job_count':job_count,
    'myFilter':myFilter}
    return render(request, 'accounts/customer.html',context)




@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def createJob(request, pk):
# 	JobFormSet = inlineformset_factory(Customer, Job, fields=('title', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = JobFormSet(queryset=Job.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = JobForm(request.POST)
# 		formset = JobFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/job_form.html', context)




def createJob(request):
    jobs_list = Job.objects.order_by('date_created')
    if request.method == "POST":
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
    print('JOB:', job)
    if request.method == 'POST':

        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/job_form.html', context)


#@allowed_users(allowed_roles=['admin'])
# def deleteJob(request, pk):
# 	job = get_object_or_404(Job, id=pk)
# 	if request.method == "POST":
# 		job.delete()
# 		return redirect('/')

# 	context = {'item':job}
# 	return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    if request.method=="POST":
        job.delete()
        return redirect('home')

        
    context = {'item':job}
    return render(request, 'accounts/delete.html', context)


# @login_required(login_url='login')
# def jobs(request):
# 	jobs = Jobs.objects.all()

# 	return render(request, 'accounts/jobs.html', {'jobs':jobs})


# @login_required(login_url='login')
# #@allowed_users(allowed_roles=['admin'])
# def employer(request, pk_test):
# 	employer = Employer.objects.get(id=pk_test)

# 	jobs = employer.job_set.all()
# 	job_count = jobs.count()

# 	myFilter = JobFilter(request.GET, queryset=jobs)
# 	jobs = myFilter.qs 

# 	context = {'customer':customer, 'jobs':jobs, 'job_count':job_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/employer.html',context)