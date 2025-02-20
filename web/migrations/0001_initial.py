# Generated by Django 5.0.7 on 2024-07-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects')),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=250)),
                ('github_link', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='skills')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
