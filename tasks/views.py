from django.shortcuts import render_to_response
from tasks.models import *

def index(request):
    return render_to_response('index.html')

def tasks(request):
    return render_to_response('tasks.html')

def task(request,task_id):
    return render_to_response('task.html')

def profile(request,user_id):
    return render_to_response('profile.html')

def people(request):
    return render_to_response('people.html')
