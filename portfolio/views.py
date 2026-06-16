from django.shortcuts import render, redirect
from .models import Project, BlogPost, ContactMessage
from django.contrib import messages
# Create your views here.


def home(request):
    if request.method == 'POST':
        # Grab the data from the HTML form input fields
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')
        
        # Save it directly into our database
        ContactMessage.objects.create(name=name, email=email, message=message_text)
        
        # Show a temporary success alert notification
        messages.success(request, "Your message has been sent successfully!")
        return redirect('home')

    # Normal page loading logic (GET request)
    projects = Project.objects.all()
    posts = BlogPost.objects.all().order_by('-created_at')
    
    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'portfolio/home.html', context)