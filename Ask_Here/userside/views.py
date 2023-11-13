from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.cache import never_cache

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
    answers = Answer.objects.filter(question=id).order_by('-id')
    user = request.user

    user_liked_answers = {}
    for answer in answers:
        user_liked_answers[answer.id] = user in answer.liked_by.all()

    if request.method == 'POST':
        answer = request.POST['answer']
        if user.is_authenticated:
            print('the user is: ',user)
            Answer.objects.create(user=user,question=query,body=answer)
            return redirect('question',id=id)
        else:
            return redirect('login')
    answers_count = answers.count()
    context = {
        'query':query,
        'answers':answers,
        'user_liked_answers': user_liked_answers,
        'answers_count':answers_count
    }
    for answer_id, liked in user_liked_answers.items():
        print(f'Answer {answer_id}: liked by user: {liked}')
    return render(request,'question.html',context)

@never_cache
def like_answer(request):
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        answer_id = request.POST.get("answer_id")
        answer = Answer.objects.get(pk=answer_id)
        user = request.user

        if user in answer.liked_by.all():
            answer.liked_by.remove(user)
            liked = False
        else:
            answer.liked_by.add(user)
            liked = True

        likes = answer.liked_by.count()

        # Check if the current user liked this answer
        user_liked = user in answer.liked_by.all()
        print('user_liked',user_liked)
        return JsonResponse({"likes": likes, "liked": liked, "user_liked": user_liked})
    else:
        return JsonResponse({"message": "Not an AJAX request"}, status=200)
    
def profile(request):
    user = CustomUser.objects.get(username=request.user)
    if request.method == 'POST':
        display_pic = request.FILES.get('profilepic')
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        bio = request.POST['bio']

        user.display_pic = display_pic
        user.first_name = first_name
        user.last_name = last_name
        user.bio = bio
        user.save()
        return redirect('profile')

    return render(request,'profile.html',{'user':user})
