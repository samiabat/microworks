from rest_framework.serializers import ModelSerializer
from .models import Job, Message, Proposal, Review, Report
from django.contrib.auth.models import User

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ProposalSerializer(ModelSerializer):
    class Meta:
        model = Proposal
        fields = '__all__'

class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'