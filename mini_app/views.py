from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Service, Project, Counter, PortfolioItem

def index(request):
    # Fetching all necessary data for the index page
    skills = Skill.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    counters = Counter.objects.all()
    portfolio_items = PortfolioItem.objects.all()

    context = {
        'skills': skills,
        'services': services,
        'projects': projects,
        'counters': counters,
        'portfolio_items': portfolio_items,
    }
    return render(request, 'index.html', context)

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create the email subject and message
        subject = f"New message from {name}"
        email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Send the email
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.RECEIVE_EMAIL],
            fail_silently=False,
        )
        return redirect('index')  # Redirect to the index page after sending the email

    return HttpResponse("Invalid request.", status=400)
