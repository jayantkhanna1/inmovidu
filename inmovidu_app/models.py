from django.db import models

# Create your models here.
class company(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
class student(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
class job(models.Model):
    position=models.CharField(max_length=300)
    requirement=models.CharField(max_length=300)
    ctc=models.CharField(max_length=300)
    cname=models.CharField(max_length=300)
    compid=models.CharField(max_length=300)
class apply(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    yop=models.CharField(max_length=300)
    resume=models.CharField(max_length=300)
    position=models.CharField(max_length=300)
    jobid=models.CharField(max_length=300)