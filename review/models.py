from django.db import models

# Create your models here.
class Org(models.Model):
	company = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Org_login(models.Model):
	company = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Services(models.Model):
	company = models.CharField(max_length=100)
	service = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	status = models.CharField(max_length=2, default='P')

class Admin(models.Model):
	username = models.CharField(max_length=100)
	email =  models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

class Admin_login(models.Model):
	username = models.CharField(max_length=100)
	password =  models.CharField(max_length=100)