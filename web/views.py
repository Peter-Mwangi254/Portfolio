from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .models import Project, Skill, Blog, Contact
from .forms import ContactForm

def home(request):
    return render(request, "web/home.html")

def about(request):
    skills = Skill.objects.all()
    context = {
        "skills":skills,
    }
    return render(request, "web/about.html", context)

def projects(request):
    projects_list = Project.objects.all().order_by("-created_on")
    context = {
        "projects": projects_list
    }
    return render(request, "web/projects.html", context)

def posts(request):
    posts_list = Blog.objects.all().order_by('-written_on')
    paginator = Paginator(posts_list, 4)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        "posts": posts,
    }

    return render(request, "web/posts.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    context = {
        "post": post,
    }

    return render(request, "web/post_detail.html", context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Message submitted successfully!")
            return redirect('home')
    else:
        form = ContactForm()
    context = {
        "form": form,
    }

    return render(request, "web/contact.html", context)


def resume(request):

    return render(request, "web/resume.html")
