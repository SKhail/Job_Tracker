from django.urls import path
from django.contrib.auth import views as auth_views
from .views import JobListCreateView
from . import views



urlpatterns = [
    path('', views.home, name='home'), 
    path('add/', views.add_job, name='add_job'),  # Adding a Job 
    path('jobs/', views.job_list, name='job_list'),  # Present all the jobs 
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'), # Edit Jobs
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),  # Delete Jobs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # login path 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # logout path
    path('signup/', views.signup, name='signup'), # Register path 
    path('note/<int:job_id>/add_note/', views.add_note, name='add_note'),     # add a note 
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),  # Delete notes
    path('api/jobs/', JobListCreateView.as_view(), name='job-list-create'),

]