from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def insert_subject(request):
    if request.method == 'POST':
        form = Insert_subject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_subject')
    form = Insert_subject()
    return render(request, 'subject/insert_subject.html', {'form': form})

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'subject/list.html', {'subjects': subjects})

def insert_major(request):
    if request.method == 'POST':
        form = Insert_major(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_major')
    form = Insert_major()
    return render(request, 'major/insert_major.html', {'form': form})

def list_major(request):
    majors = Major.objects.all()
    return render(request, 'major/list_major.html', {'majors': majors})

def edit_major(request, id):
    if request.method == 'POST':
        major = Major.objects.get(id=id)
        form = Edit_major(request.POST, instance=major)
        if form.is_valid():
            form.save()
            return redirect('list_major')
    major = Major.objects.get(id=id)
    form = Edit_major()
    return render(request, 'major/edit_major.html', {'form': form})


def insert_student(request):
    if request.method == 'POST':
        form = Insert_student(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = Insert_student()
    return render(request, 'student/insert_student.html', {'form': form})

def list(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()
    return render(request, 'list.html', {'majors': majors, 'subjects': subjects, 'students': students})