from django.shortcuts import render
from django .views.generic import ListView ,DetailView
from .models import Job,FeaturedJobs
# Create your views here.



class Job(ListView):
    model =Job


class FeatureJobs(DetailView):
    model = FeaturedJobs   
