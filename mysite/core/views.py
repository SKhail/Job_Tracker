from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login
from sorting.sorting_jobs import SortRecent, SortOldest  # Sorting Job Posts 
from filtering.filtering_jobs import StatusFilter   # Filtering Job Post 

from rest_framework import generics 
from .serializers import JobSerializers


from .forms import JobForm
from .models import Job

from .forms import NoteForm
from .models import Note

def home(request):
    return render(request, 'home.html')

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hooray! Job added ✅")
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

# update jobs by providing a edit feature
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Hooray! Job Updated ✅")
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form' : form})


# Delete Jobs
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        job.delete()
        messages.success(request, "Jobs has been 🗑️")
        return redirect('job_list')
    
    return render(request, 'delete_job.html', {'job': job})

# Job lists 
@login_required
def job_list(request):
    sorting_jobs = request.GET.get('sort', 'recent')

    sorting =  SortOldest() if sorting_jobs == 'oldest' else SortRecent()
    jobs =  sorting.sort(Job.objects.all()) # Getting the data and sorting it

    status_filter = StatusFilter()
    jobs =  status_filter.apply(jobs, request) # Getting the data and apply filtering feature 
    
    paginator = Paginator(jobs, 5) # Show 5 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'job_list.html', {'page_obj': page_obj})
 
# User to be able to log in
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Option for users to login immedately 
            messages.success(request, "Account Created! ✅")
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form' : form})


# For creating notes in job posts
@login_required
def add_note(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = NoteForm(request.POST) 
    if form.is_valid():
        note = form.save(commit=False)
        note.job = job
        note.user = request.user
        note.save()
        messages.success(request, "You have Succesfully added a 📝")
        return redirect('job_list')
    else:
        form = NoteForm()
        return render(request, 'add_note.html', {'form': form})

# Deleting a note in the job post
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    # Adding Security Layer to give protection for users
    if  note.user != request.user:
        messages.error(request, "You are not allowed to delete this note.")
        return redirect('job_list')
    
    if request.method == 'POST':
        note.delete()
        messages.success(request, "Note has been 🗑️")
        return redirect('job_list')
    return render(request, 'delete_note.html', {'note': note})


# Creating API to push to frontend
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializers