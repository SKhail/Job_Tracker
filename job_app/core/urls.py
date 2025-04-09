from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('add/', views.add_job, name='add_job'),  # Adding a Job 
    path('jobs/', views.job_list, name='job_list'),  # Present all the jobs 
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'), # Edit Jobs
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job')  # Delete Jobs
    
]