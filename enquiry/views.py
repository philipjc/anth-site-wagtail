from django.shortcuts import redirect
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.http import Http404
from django.core.mail import send_mail

from django.urls import reverse_lazy

import sendgrid
import os
from sendgrid.helpers.mail import *
from decouple import config


def send_enquiry(request):
    url = request.POST.get('url', None)
    name = request.POST.get('enquiry_name', '')
    form_email = request.POST.get('enquiry_email', '')
    text = request.POST.get('enquiry_text', '')

    if form_email == '':
        raise Http404

    else:

        send_mail('Your Drishti Enquiry', text, form_email,
                  [settings.CLIENT_EMAIL])

        return redirect(reverse_lazy('enquiry:thanks'))

# SendGrid API
    # else:
    #     sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))
    #     from_email = Email("philipcox83@gmail.com")
    #     to_email = Email("filystyle@gmail.com")
    #     subject = "Sending with SendGrid is Fun"
    #     email_content = Content("text/plain", "and easy to do anywhere, even with Python")
    #     new_mail = Mail(from_email, subject, to_email, email_content)
    #     response = sg.client.mail.send.post(request_body=new_mail.get())
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    #     print('ko')
    #
    #     return redirect(reverse_lazy('enquiry:thanks'))

# Old Way
    # else:
    #     plaintext = get_template('enquiry/emails/enquiry.txt')
    #     html = get_template('enquiry/emails/enquiry.html')
    #
    #     d = dict({
    #         'name': name,
    #         'email': form_email,
    #         'text': text,
    #     })
    #
    #     # subject, from_email, to = 'News Letter Signup Request', email, settings.CLIENT_EMAIL
    #     subject, from_email, to = 'Enquiry from site visitor', email, settings.CLIENT_EMAIL
    #     text_content = plaintext.render(d)
    #     html_content = html.render(d)
    #     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()
    #
    #     return redirect(reverse_lazy('enquiry:thanks'))
