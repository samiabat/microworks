from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user','email']

class JobForm(ModelForm):
	class Meta:
		model = Job
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'email', 'password1', 'password2']
class ProposalForm(ModelForm):
	class Meta:
		model = Proposal
		fields = '__all__'

