from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    questions = Question.objects.all().order_by('-id')
    if request.method == 'POST':
        query = request.POST['query']
        user=request.user
        question = Question.objects.create(user=user,query=query)
        return redirect('home')
    background_colors = ['one', 'two', 'three', 'four']
    context = {
        'questions':questions,
        'background_colors':background_colors
    }
    return render(request,'home.html',context)

def question(request,id):
    query = Question.objects.get(id=id)
    return render(request,'question.html',{'query':query})