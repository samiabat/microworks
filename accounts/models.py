from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
	STATUS = (
			('beginer', 'beginer'),
			('intermidate', 'intermidate'),
			('expert', 'expert'),
			)
	title = models.CharField(max_length=200, null = True)
	customer = models.CharField(max_length=50, null = True)
	description = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	salary = models.IntegerField(null=True)


class Proposal(models.Model):
	jobApplyer = models.CharField(max_length = 50, null = True)
	proposal = models.TextField(null=True)
	email = models.EmailField(max_length = 50, null = True)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)

