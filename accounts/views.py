from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.db.models import Q, Count
from django.http.response import JsonResponse

from .models import Job, Proposal, Review, Report
from .serializer import CustomerSerializer, JobSerializer, MessageSerializer, ProposalSerializer, ReportSerializer, ReviewSerializer # ReportSerializer, ReviewSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profileApi(request, format=None):
    if request.user!="AnonymousUser":
        try:
            content = {
                'user': str(request.user),
                'role': str(request.user.groups.all()[0]),  
                'id': str(request.user.id),
            }
            return Response(content)
        except:
            content = {
                'user': str(request.user),
                'role': "admin",  
            }
            return Response(content)
    



@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
def customerApi(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            users = User.objects.all()
            users_serializer = CustomerSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            try:
                user = User.objects.get(id=pk)
                if user is not None:
                    user_serializer = CustomerSerializer(user)
                    return JsonResponse(user_serializer.data, safe=False)
            except:
                return JsonResponse("No Such User!", safe=False) 
        
    elif request.method == "POST":
        customer_data = JSONParser().parse(request)
        try :
            other_customer = User.objects.get(username = customer_data["username"])
            if other_customer:
                return JsonResponse("The User Name Already Exist!", safe=False)
        except:
            customer_data["password"] = make_password(customer_data["password"])
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return JsonResponse("User Register Sucessfully!", status=201, safe=False)
            return JsonResponse("Failed To Register!", status=400, safe=False)
    
    elif request.method == "PUT":
        customer_data = JSONParser().parse(request)
        try:
            customer = User.objects.get(id = pk)
            customer_data["password"] = make_password(customer_data["password"])
            customer_serializer = CustomerSerializer(customer, data=customer_data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return JsonResponse("Data Updated Sucessfully!", safe=False)
            return JsonResponse("Unable To Update!", safe=False)
        except:
            return JsonResponse("The Same ID Is Already In Use!", safe=False)
    elif request.method == "DELETE":
        try:
            customer = User.objects.get(id=pk)
            if customer:
                customer.delete()
                return JsonResponse("Data Deleted Sucessfully!", safe=False)
        except:
            return JsonResponse("No Such User!", safe=False)


@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def jobApi(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            jobs = Job.objects.all().order_by('-date_created')
            jobs_serializer = JobSerializer(jobs, many=True)
            return JsonResponse(jobs_serializer.data, safe=False)
        else:
            try:
                job = Job.objects.get(id=pk)
                if job is not None:
                    job_serializer = JobSerializer(job)
                    return JsonResponse(job_serializer.data, safe=False)
            except:
                return JsonResponse("No Such Job!", safe=False) 
        
    elif request.method == "POST":
        job_data = JSONParser().parse(request)
        job_serializer = JobSerializer(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse("Job Posted Sucessfully!", status=201, safe=False)
        return JsonResponse("Failed To Post!", status=400, safe=False)
    elif request.method == "PUT":
        job_data = JSONParser().parse(request)
        try:
            job = Job.objects.get(id=pk)
            job_serializer = JobSerializer(job, data=job_data)
            if job_serializer.is_valid():
                job_serializer.save()
                return JsonResponse("job Update Sucessfully!", safe=False)
        except:
            return JsonResponse("Failed To Update!", safe=False)
    elif request.method == "DELETE":
        try:
            print(id)
            job = Job.objects.get(id=pk)
            if job is not None:
                job.delete()
                return JsonResponse("job Deleted Sucessfully!", safe=False)
        except:
            return JsonResponse("No Such job!", safe=False)


@csrf_exempt
@api_view (['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def proposalApi(request, pk=-1):
    if request.method == "GET":
        if pk==-1:
            proposals = Proposal.objects.all().order_by('-date_created')
            proposal_serializer = ProposalSerializer(proposals, many=True)
            return JsonResponse(proposal_serializer.data, safe=False)
        else:
            try:
                proposal = Proposal.objects.get(id=pk)
                if proposal is not None:
                    proposal_serializer = ProposalSerializer(proposal)
                    return JsonResponse(proposal_serializer.data, safe=False)
            except:
                return JsonResponse("No Such Proposal!", safe=False) 
        
    elif request.method == "POST":
        proposal_data = JSONParser().parse(request)
        proposal_serializer = ProposalSerializer(data=proposal_data)
        if proposal_serializer.is_valid():
            proposal_serializer.save()
            return JsonResponse("Proposal submitted successfully!", status=201, safe=False)
        return JsonResponse("Failed To submit!", status=400, safe=False)
    elif request.method == "PUT":
        proposal_data = JSONParser().parse(request)
        try:
            proposal = Proposal.objects.get(id=pk)
            proposal_serializer = ProposalSerializer(proposal, data=proposal_data)
            if proposal_serializer.is_valid():
                proposal_serializer.save()
                return JsonResponse("Proposal Update Sucessfully!", safe=False)
        except:
            return JsonResponse("Failed To Update!", safe=False)
    elif request.method == "DELETE":
        try:
            proposal = Proposal.objects.get(id=pk)
            if proposal is not None:
                proposal.delete()
                return JsonResponse("Proposal Deleted Sucessfully!", safe=False)
        except:
            return JsonResponse("No Such Proposal!", safe=False)



@csrf_exempt
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def getProposalByJob(job):
    try:
        proposals = User.objects.filter(job = job)
        proposal_serializer = ProposalSerializer(proposals, many=True)
        return JsonResponse(proposal_serializer.data, safe=False)
    except:
        return JsonResponse("Not Authenticated!", safe=False)

@csrf_exempt
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def getReview(id):
    try:
        review = Review.objects.annotate(
        totalReview=Count('reviews', filter=Q(reviews__jobPoster=id))
        )
        return JsonResponse(review, safe=False)
    except:
        return JsonResponse("Not Authenticated!", safe=False)

@csrf_exempt
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def getReport(id):
    try:
        report = Report.objects.annotate(
        totalReport=Count('reports', filter=Q(reports__jobPoster=id))
        )
        return JsonResponse(report, safe=False)
    except:
        return JsonResponse("Not Authenticated!", safe=False)





@csrf_exempt
@api_view (['POST'])
@permission_classes([IsAuthenticated])
def review(request):
    review_data = JSONParser().parse(request)
    try :
        other_review = Review.objects.get(jobPoster = review_data["jobPoster"], job = review_data["job"])
        if other_review:
            return JsonResponse("You have already reviewed!", safe=False)
    except:
        review_serializer = ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Your review submitted succusfully!", status=201, safe=False)
        return JsonResponse("Something went wrong!", status=400, safe=False)

@csrf_exempt
@api_view (['POST'])
@permission_classes([IsAuthenticated])
def report(request):
    report_data = JSONParser().parse(request)
    report = Report.objects.filter(jobPoster=report_data["jobPoster"], job=report_data["job"]).count()
    if report!=0:
        return JsonResponse("You have already reported!", safe=False)
    else:
        report_serializer = ReportSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse("Your report submitted succusfully!", status=201, safe=False)
        return JsonResponse("Something went wrong!", status=400, safe=False)
        

def getUserByusername(request, username):
    try:
        user = User.objects.get(username=username)
        users_serializer = CustomerSerializer(user)
        return JsonResponse(users_serializer.data, safe=False)
    except:
        return JsonResponse("Something went wrong!", safe=False)

@csrf_exempt
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def reporting(request, id):
    report = Report.objects.filter(jobPoster=id).count()
    return JsonResponse(report, safe=False)


@csrf_exempt
@api_view (['POST'])
@permission_classes([IsAuthenticated])
def message(request):
    message_data = JSONParser().parse(request)
    message_serializer = MessageSerializer(data=message_data)
    if message_serializer.is_valid():
        message_serializer.save()
        return JsonResponse("message sent!", status=201, safe=False)
    return JsonResponse("Something went wrong!", status=400, safe=False)

@csrf_exempt
@api_view (['GET'])
@permission_classes([IsAuthenticated])
def getMessage(someone):
    try:
        messages = User.objects.filter(jobPoster = someone)
        message_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(message_serializer.data, safe=False)
    except:
        return JsonResponse("Not Authenticated!", safe=False)

