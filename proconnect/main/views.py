from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User

def home(request):
    return render(request, 'main/index.html')

def base(request):
    return render(request, 'main/base.html')

def signIn(request):
    return render(request, 'main/sign-in.html')

def signup(request):
    return render(request, 'main/sign-up.html')

def landingpage(request):
    return render(request, 'landingpage/index.html')

def complete_profile(request):
    return render(request, 'main/complete_login.html')

def google_oauth2_complete(request):
    user = request.user
    
    if user.is_authenticated and UserSocialAuth.objects.filter(user=user, provider='google-oauth2').exists():
        return redirect('feed_page_name')
    else:
        if user.is_authenticated:
            UserSocialAuth.objects.create(user=user, provider='google-oauth2')
        else:
            user = User.objects.create_user(username='new_user', password='random_password')
            UserSocialAuth.objects.create(user=user, provider='google-oauth2')
            return redirect('login')
        
        return redirect('feed_page_name')
