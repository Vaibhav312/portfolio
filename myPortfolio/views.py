from django.shortcuts import render
from myPortfolio.forms import ContactUsForm
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Create your views here.
def index(request):
        if request.method== "POST":
            contact=ContactUsForm(data=request.POST)
            if contact.is_valid():
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('email', '')
                    total_message=from_email+'\n'+subject+'\n'+message
                    print(total_message)
                    contact.save()
                    try:
                        
                        send_mail(subject, total_message, from_email, ['vaibhavbaghel3196@gmail.com'])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'Thanks for contacting me',extra_tags='alert')
                    return HttpResponseRedirect('/')
                   
        else:
            contact = ContactUsForm()
        return render(request,'index.html',context={'contacts':contact})

 