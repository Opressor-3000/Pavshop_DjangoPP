from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from .utils import account_activation_token
from django.conf import settings


def send_email(user, current_site):
   subject = 'Activate Your Pavshop.com Account'
   message = render_to_string('account/activation.html', {
      'user': user,
      'domain': current_site.domain,
      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      'token': account_activation_token.make_token(user),
   }) 
   mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[user.email,])
   mail.content_subtype="html"
   mail.send()