# Generated by Django 4.2.17 on 2024-12-18 14:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='post_images')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_likes', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('DENIED', 'DENIED'), ('ALLOWED', 'ALLOWED'), ('PENDING', 'PENDING')], default='PENDING', max_length=10)),
                ('talent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PostRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
                ('ratings', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TalentOfTheMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id_user', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, default='')),
                ('profileimg', models.ImageField(default='blank-profile-picture.png', upload_to='profile_images')),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
