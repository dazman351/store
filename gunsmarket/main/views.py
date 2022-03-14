from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, AuthUserForm, ProfileEditForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile



def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, "main/index.html", data)

def about(request):
    return render(request, "main/about.html")

def info(request):
    return render(request, "main/info.html")


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})




class Login(LoginView):
    template_name = 'main/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('home')
    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    next_page = reverse_lazy('home')



def user_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    if id != request.user.profile.id:
        return redirect('error_page')
    return render(request, 'main/user_profile.html', {'profile': profile})




def edit_profile(request, id):
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    if id != request.user.id:
        return redirect('error_page')
    context = {'form': form }
    return render(request, 'main/edit_profile.html', context)


def error_page(request):
    return render(request, 'main/error_page.html')