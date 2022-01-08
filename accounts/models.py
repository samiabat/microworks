from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
	st = (
			('Freelancer', 'Freelancer'),
			('Employer', 'Employer'),
			)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	stat = models.CharField(max_length=200, null=True, choices=st)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return self.name

# class Product(models.Model):
# 	CATEGORY = (
# 			('Indoor', 'Indoor'),
# 			('Out Door', 'Out Door'),
# 			) 

# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField(null=True)
# 	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
# 	description = models.CharField(max_length=200, null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	tags = models.ManyToManyField(Tag)

	# def __str__(self):
	# 	return self.name

class Job(models.Model):
	STATUS = (
			('beginer', 'beginer'),
			('intermidate', 'intermidate'),
			('expert', 'expert'),
			)

	title = models.CharField(max_length=200, null = True)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	note = models.CharField(max_length=1000, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	salary = models.IntegerField(null=True)

	def __str__(self):
		return str(self.title)

# class Employer(models.Model):
# 	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=200, null=True)
# 	phone = models.CharField(max_length=200, null=True)
# 	email = models.CharField(max_length=200, null=True)
# 	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name
# class Job(models.Model):
# 	STATUS = (
# 		('Beginer', 'Beginer'), 
# 		('Intermidate', 'Intermediate'),
# 		('Expert', 'Expert'),
# 	# 	)
	# employer = models.ForeignKey(Employer, null=True, on_delete= models.SET_NULL)
	# title = models.CharField(max_length = 250, null=True)
	# date_created = models.DateTimeField(auto_now_add=True, null=True)
	# status = models.CharField(max_length=200, null=True, choices=STATUS)
	# description = models.TextField(null=True)
	# salary = models.IntegerField(null=True)





# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()