# from django import urls
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from utils.tokenGenerator import generate_token
# from django.core.mail import send_mail
# from django.conf import settings


# def send_activation_email(user, request):
#     current_site = get_current_site(request)
#     email_subject = "Ative a sua conta"
#     email_body = render_to_string('register/activate.html',
#                                   {
#                                       'user': user,
#                                       'domain': current_site,
#                                       'uid': urlsafe_base64_encode(force_bytes(user.id)),
#                                       'token': generate_token.make_token(user)
#                                   })

#     send_mail(email_subject,
#               email_body,
#               settings.EMAIL_HOST_USER,
#               [user.email],
#               fail_silently=False)
