from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import JobForm
from .models import Job

def home(request):
    return render(request, 'home.html')

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hooray! Job added ✅")
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all() # Get all the mobs from the database
    return render(request, 'job_list.html', {'jobs': jobs}) 


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