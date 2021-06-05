from django.shortcuts import render,redirect
from .models import Job
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
 
def add(request):
    Jobrole=request.POST["Jobrole"]
    Qualification=request.POST["Qualification"]

    Specialisation =request.POST["Specialisation"]
    Location=request.POST["Location"]
    Salary=request.POST["Salary"]
    ApplyDate=request.POST["ApplyDate"]
    
    ins=Job(Jobrole=Jobrole,Qualification=Qualification,Specialisation=Specialisation,Location=Location,Salary=Salary,ApplyDate=ApplyDate)
    ins.save()
    return redirect('index')

def hubli(request):
    jobs= Job.objects.all()
    return render(request, 'display.html', {'jobs': jobs})
    

def roles(request):
    
    h1= Job.objects.all()
    return render(request, 'job.html', {'h1': h1})

    
