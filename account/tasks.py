from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from .utils import account_activation_token
from pavshop import settings


def send_email(user, current_site):
   subject = 'Actovate Your Pavshop.com Account'
   message = render_to_string('activation.html', {
      'user': user,
      'domain': current_site.domain,
      'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      'token': account_activation_token.make_token(user),
   }) 

   sender = settings.EMAIL_HOST_USER
   recipent = user.email
   mail = EmailMultiAlternatives(subject, body=message, from_email=recipent, to=[recipent],)
   mail.attach_alternative(message, 'text/html')
   mail.send()