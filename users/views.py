from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .forms import UserCreationForm,UserUpdateForm
from django.contrib import messages



# Create your views here.

class Registertion(View):
    def get(self,request):
        create_form = UserCreationForm()
        context = {
            "form": create_form
        }
        return render(request, 'users/singup.html', context)

    def post(self,request):
        create_form=UserCreationForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('home')
        else:
            context={
                "form":create_form
            }
            return render(request,'users/singup.html',context)






class Home(TemplateView):
    template_name = 'home.html'


class LoginView(View):

    def get(self,request):
        user_login = AuthenticationForm()
        return  render(request,'users/login.html',{'user_login':user_login})

    def post(self,request):
        user_login=AuthenticationForm(data=request.POST)
        if user_login.is_valid():
            user=user_login.get_user()
            login(request,user)
            messages.success(request,'You have successfully logged in')
            return redirect('books:Listview')
        else:
            return render(request, 'users/login.html',{'user_login':user_login})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'users/profile.html',{"user":request.user})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
         logout(request)
         messages.info(request,'You have successfully logged out.')
         return redirect('home')


class UserUpadeView(LoginRequiredMixin,View):
    def get(self,request):
        user_update_form=UserUpdateForm(instance=request.user)
        return render(request,'users/profile_edit.html',{'form':user_update_form})
    def post(self,request):
        user_update_form=UserUpdateForm(instance=request.user,data=request.POST)

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,'You have successfully updated your profile.')
            return  redirect('users:profile')
        return render(request,'users/profile_edit.html',{'form':user_update_form})


