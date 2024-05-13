from django.db import models
from django.utils.text import slugify
import string
import random
from random import randint

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=2000)
	message = models.TextField()

	def __str__ (self):
		return self.name

class Post(models.Model):
	name = models.CharField(max_length=200)
	occupation = models.CharField(max_length=2000)
	price = models.CharField(max_length=200,default='0',blank=True)
	country = models.CharField(max_length=200,default='0',blank=True)
	gender = models.CharField(max_length=200,default='0',blank=True)
	image = models.FileField(blank=True)
	dob = models.DateField(blank=True,null=True)
	comment = models.TextField(blank=True)
	slug = models.SlugField(blank=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Post, self).save(*args, **kwargs)

	def __str__ (self):
		return self.name

class Booking(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
	price = models.CharField(max_length=200,default='0',blank=True)
	email = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200,default='0')
	job = models.CharField(max_length=200,default='0')
	sex = models.CharField(max_length=200,default='0')
	home = models.CharField(max_length=200,default='0')
	air = models.CharField(max_length=200,default='0')
	phone = models.CharField(max_length=200,default='0')
	type_event = models.CharField(max_length=200,default='0')
	active = models.BooleanField(default=False)
	date = models.DateField(blank=True,null=True)
	message = models.TextField()
	
	def __str__(self):
		return self.email

class Ticket(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
	date = models.CharField(max_length=200)
	live = models.CharField(max_length=200)
	price = models.CharField(max_length=200,default='0')
	location = models.CharField(max_length=200)
	time = models.CharField(max_length=400, blank=True)
	
	def __str__(self):
		return self.live

class Ticbooking(models.Model):
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, default='')
	email = models.CharField(max_length=200)
	active = models.BooleanField(default=False)
	pin = models.CharField(max_length=200)
	
	def __str__(self):
		return self.pin

class Card(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	sex = models.CharField(max_length=200)
	phone = models.CharField(max_length=200,default='0')
	address = models.CharField(max_length=200,default='0')
	date = models.DateField(auto_now_add=True)
	active = models.BooleanField(default=False)
	pin = models.CharField(max_length=200)
	image = models.FileField(blank=True)

	def __str__(self):
		return self.name