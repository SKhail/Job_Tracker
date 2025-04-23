from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login
from sorting.sorting_jobs import SortRecent, SortOldest  # Sorting Job Posts 
from .forms import JobForm
from .models import Job






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

    if sorting_jobs == 'oldest':
        sorting = SortOldest()
    else:
        sorting = SortRecent() # It will be default

    jobs =  sorting.sort(Job.objects.all()) # Getting the data and sorting it

    status_filter = request.GET.get('status')
    if status_filter:
        jobs = Job.filter(status=status_filter)

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

# Testing the add job form 
def test_view(request):
    if request.method == 'POST':
        print("Form Sucessful")
    return render(request, 'test.html')

