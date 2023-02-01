from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
class LoginView(View):
    '''This function manage user login process.'''
    def get(self,request):
        return render(request, 'userauth/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check username and password combination is correct or not.
        authuser = authenticate(username=username, password=password)
        if authuser is not None:
            return render(request, 'dashboard/dashboard.html')
        else:
            return render(request, 'userauth/login.html')






class RegisterView(View):
    def get(self,request):
        return render(request, 'userauth/register.html')


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        authuser = authenticate(username=username, password=password)
        if authuser is not None:
            return render(request, 'dashboard/dashboard.html')
        else:
            user = User.objects.create_user(username=username,)
            user.set_password('password')
            user.save()
            return render(request, 'userauth/login.html')