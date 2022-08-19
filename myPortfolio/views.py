<<<<<<< HEAD

=======
>>>>>>> 10291a68373980a779da1d8a03c9eee854178d9c
from django.shortcuts import render
from myPortfolio.forms import ContactUsForm
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
<<<<<<< HEAD
from decouple import config
=======
>>>>>>> 10291a68373980a779da1d8a03c9eee854178d9c


# Create your views here.
def index(request):
        if request.method== "POST":
            contact=ContactUsForm(data=request.POST)
            if contact.is_valid():
<<<<<<< HEAD
                    name = request.POST.get('name', '')
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('email', '')
                    total_message=f"Greetings from MyPortfolio!\n\nHey {name}\nOne user has approached us with below details\n\nUser email:{from_email}\nSubject:{subject}\nMessage:{message}\n\nThanks and Regards\nMy Portfolio Team"
                    # total_message=from_email+'\n'+subject+'\n'+message
                    EMAIL_HOST_USER=config('EMAIL_HOST_USER')
                    print("subject",subject)
                    print("message",message)
                    print("from_email",from_email)
                    print("total_message",total_message)
                    print("EMAIL_HOST_USER",EMAIL_HOST_USER)
=======
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('email', '')
                    total_message=from_email+'\n'+subject+'\n'+message
                    print(total_message)
>>>>>>> 10291a68373980a779da1d8a03c9eee854178d9c
                    contact.save()
                    try:
                        
                        send_mail(subject, total_message, from_email, ['vaibhavbaghel3196@gmail.com'])
<<<<<<< HEAD
           
=======
>>>>>>> 10291a68373980a779da1d8a03c9eee854178d9c
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'Thanks for contacting me',extra_tags='alert')
                    return HttpResponseRedirect('/')
                   
        else:
            contact = ContactUsForm()
        return render(request,'index.html',context={'contacts':contact})

 