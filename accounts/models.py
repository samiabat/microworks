from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
	st = (
			('Freelancer', 'Freelancer'),
			('Employer', 'Employer'),
			)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	stat = models.CharField(max_length=200, null=True, choices=st)
	username = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True, unique=True)
	phone = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	Bio = models.TextField(blank=True)

	def __str__(self):
		return self.username


class Job(models.Model):
	STATUS = (
			('beginer', 'beginer'),
			('intermidate', 'intermidate'),
			('expert', 'expert'),
			)

	title = models.CharField(max_length=200, null = True)
	customer = models.CharField(max_length=50, null = True)
	email = models.EmailField(max_length=40, null = True)
	description = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	salary = models.IntegerField(null=True)
	jobCode = models.CharField(max_length=20, unique=True, null=True)

	def __str__(self):
		return str(self.title)

class Proposal(models.Model):
	jobApplyer = models.CharField(max_length = 50, null = True)
	proposal = models.TextField(null=True)
	email = models.EmailField(max_length = 50, null = True)
	jobCode = models.CharField(max_length=20, null = True)

