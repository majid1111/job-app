from django.db import models

# Create your models here.


GENDER_CHOICES = (
       ('Male','Male'),
       ('Fmale','Fmale'),
   )



class Job(models.Model):
    name_of_job = models.CharField(max_length=20 )
    desriptionJob = models.CharField(max_length=200)
    part_of_time = models.CharField(max_length=50)





class FeaturedJobs (models.Model):
    name = models.CharField(max_length=100)
    experince = models.IntegerField()   
    certificate = models.CharField(max_length=20)
    salary = models.FloatField()
    tranining = models.IntegerField()
    male_or_female= models.BooleanField(max_length=10,choices=GENDER_CHOICES)
