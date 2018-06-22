from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from .models import Utilisateur

@login_required
def logout_fct(request):
    logout(request)
    return redirect("/")


def login_user(request):
    if len(request.POST)>0:
        post = request.POST
        user = authenticate(username=post["username"], password=post["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def create_account(request):
    if len(request.POST) > 0:
        try:
            post = request.POST
            if post["password"] == post["confirm"]:
                user = User.objects.create_user(post["username"], post["email"], post["password"])
                user.last_name = post["name"]
                myfile = request.FILES['avatar']
                util = Utilisateur()
                util.user = user
                util.avatar = myfile
                util.credit = 10000
                user.save()
                util.save()
                return redirect('/')
            else:
                return render(request, 'signin.html', {'msg': "Les mots de passes ne sont pas identique"})
        except Exception as e:
            return render(request, 'signin.html', {'msg': e})
    else:
        return render(request, 'signin.html')
