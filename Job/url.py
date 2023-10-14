from django.urls import path
from .views import Job, FeatureJobs


urlpatterns= [
path('', Job.as_view()),
path('FeatureJob',FeatureJobs.as_view()),

]