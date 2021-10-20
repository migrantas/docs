from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View

class Index(View):
    def get(self, request):
        return render(request, "index.html")
class Login(View):
    def post(self, request):
        username = request.POST.get('login').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        err = ""
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            err = "Пользовтеля не сущеcтвует"
            return render(request, "login.html", context={'error': err})

    def get(self, request):
        return render(request, "login.html")
# Create your views here.
