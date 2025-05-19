import json
import firebase_admin
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from firebase_admin import credentials, auth as firebase_auth
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.

if not firebase_admin._apps:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cred_path = os.path.join(current_dir, 'codeshrine-efc69-firebase-adminsdk-fbsvc-d73aa3234a.json')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

@csrf_exempt
def google_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            id_token = data.get('idToken')
            if not id_token:
                return JsonResponse({'error': 'No ID token provided'}, status=400)

            decoded_token = firebase_auth.verify_id_token(id_token)
            email = decoded_token.get('email')
            name = decoded_token.get('name', '')
            uid = decoded_token.get('uid')

            if not email:
                return JsonResponse({'error': 'No email in token'}, status=400)

            # Try to find user by email or create one
            user, created = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': name})

            # Log the user in
            login(request, user)

            return JsonResponse({'status': 'success'})
        
        except Exception as e:
            print("Google Login Error:", e)
            return JsonResponse({'error': 'Token verification failed'}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)

def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User with this username already exists')
            return redirect("/auth/register/")
        
        user = User.objects.create_user(username=username)

        user.set_password(password)

        user.save()
        
        messages.info(request,'User created successfully')
        return redirect('/auth/register/')
    
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
    

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login')
        

        login(request,user)
        messages.info(request,'login successful')

        return redirect('/')
    
    template = loader.get_template('login.html')
    context ={}
    return HttpResponse(template.render(context,request))

def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')