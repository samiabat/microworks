from rest_framework.serializers import ModelSerializer
from .models import Job, Proposal
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