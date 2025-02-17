# define all models within the web app
from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Project(models.Model):
    # model to display a project title, image/link to project/ link to github files, technologies
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projects")
    description = RichTextField()
    link = models.URLField(max_length=250)
    github_link = models.URLField(max_length=250, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    icon = models.ImageField(upload_to="skills")
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title

class Blog(models.Model):
    """model for blog"""
    title = models.CharField(max_length=250)
    body = RichTextField()
    slug = AutoSlugField(unique=True, populate_from='title', blank=True)
    written_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    """All contacts"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=150)
    body = models.TextField()
    submitted_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " " + self.subject

