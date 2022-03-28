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

	def __str__(self):
		return self.title


class Proposal(models.Model):
	jobApplyer = models.CharField(max_length = 50, null = True)
	proposal = models.TextField(null=True)
	job = models.ForeignKey(Job, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Message(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE)
	receiver = models.CharField(max_length=200, null = True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Report(models.Model):
	id = models.AutoField(primary_key=True)
	jobPoster = models.ForeignKey(User, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.DO_NOTHING)

class Review(models.Model):
	id = models.AutoField(primary_key=True)
	jobPoster = models.ForeignKey(User, on_delete=models.CASCADE)
	job = models.ForeignKey(Job, on_delete=models.DO_NOTHING)
