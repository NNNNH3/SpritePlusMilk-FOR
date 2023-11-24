from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from core import models, forms
from django.contrib import messages


def literally1984(request):
    if request.user.is_authenticated and not models.Profile.filter(user=request.user).exists():
        return redirect('core:cr_profile')

def sign_up(request):

    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            print(form.data)
            form.save()
            messages.success(request, f'Учётная запись создана')
            return redirect('core:home')

    context = {
        'form': forms.UserCreateForm()
    }
    return render(request=request, template_name='core/sign_up.html', context=context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:home')

        else:
            messages.info(request, 'Логин либо пароль введены неверно')
            return render(request=request, template_name='core/sign_in.html')

    return render(request=request, template_name='core/sign_in.html')


def logout_user(request):
    logout(request)
    return redirect('core:home')


def create_profile(request):

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            gett = models.Profile.objects.get(user=request.user),
            profile = gett[0]
            if patronymic := form.data.get('patronymic'):
                print(profile)

                profile.patronymic = patronymic
            if phone_number := form.data.get('phone_number'):
                profile.phone_number = phone_number
            if date_of_birth := form.data.get('date_of_birth'):
                profile.date_of_birth = date_of_birth

            profile.save()
            messages.success(request, f'заебись')
            return redirect('core:home')

    context = {
        'form': forms.ProfileForm()
    }
    return render(request=request, template_name='core/create_profile.html', context=context)

class Home(TemplateView):
    template_name = 'core/home.html'

