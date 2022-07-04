from base64 import urlsafe_b64decode
import re
import threading
from django.shortcuts import render, redirect
from forms.register.registerForm import CreateUserForm
from .models import UserModel
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
from utils.tokenGenerator import generate_token
from django import urls
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from bll.emailSender.emailSender import EmailThread
# Renders register page and and handles users registation

def register(request):
    if request.method == "GET":
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'register/register.html', context)
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            print(first_name, last_name, username, email)
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                raw_password = form.cleaned_data['password1']
                data = UserModel(first_name=first_name,
                                 last_name=last_name,
                                 username=username,
                                 email=email,
                                 )
                data.set_password(raw_password)  # encrypts passwords
                data.save()
                send_activation_email(data, request)
                messages.add_message(
                    request, messages.SUCCESS, 'Por favor,aceda ao seu email para verificar a sua conta!')
                return redirect('/login')
            else:
                messages.info(request, 'invalid registration details')
        return render(request, 'register/register.html', context)

#Send user activation link using he's email address
def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Ative a sua conta"
    email_body = render_to_string('register/activate.html',
                                  {
                                      'user': user,
                                      'domain': current_site,
                                      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                      'token': generate_token.make_token(user)
                                  })

    email = EmailMessage(subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email])

    EmailThread(email).start()


#Activates user after he confirms he's email
def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(id=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Email verificado')
        return redirect(reverse('login'))

    return render(request, 'register/activation_failed.html', {"user": user})
