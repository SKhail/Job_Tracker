from django.urls import path
from django.contrib.auth import views as auth_views
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

]