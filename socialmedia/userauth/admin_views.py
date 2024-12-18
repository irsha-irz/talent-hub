from django.utils import timezone
from django.db.models import Sum
from .models import TalentOfTheMonth, Post
from itertools import chain
from django.shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.utils import timezone
from django.db.models import Sum
from .models import TalentOfTheMonth,Profile
from django.core.management import call_command

@login_required(login_url='/loginn')
def talent_of_the_month(request):
    user = User.objects.filter(username=request.user.username).first()
    if (user.is_superuser == True):
        call_command('generate_talent_of_the_month')
        return redirect('/')
    else:
        print("User is not an admin")
        invalid="Not Authorized"
        return render(request, 'loginn.html',{'invalid':invalid})
    
@login_required(login_url='/loginn')
def denied(request):
    user = User.objects.filter(username=request.user.username).first()
    if (user.is_superuser == True):
        post=Post.objects.filter(status="DENIED").order_by('-created_at')
        profile = Profile.objects.get(user=request.user)
        context={
            'post':post,
            'profile':profile
            
        }
        return render(request, 'denied.html',context)
    else:
        invalid="Not Authorized"
        return render(request, 'loginn.html',{'invalid':invalid})

@login_required(login_url='/loginn')
def talents(request):
    user = User.objects.filter(username=request.user.username).first()
    if (user.is_superuser == True):
        final_posts = []
        
        talents = TalentOfTheMonth.objects.all().order_by('-creation_date')
        #print(f"talent: {talents.post}")
        for talent in talents:
            post_data = {
                'id': talent.post.id,
                'user': talent.post.user,
                'image': talent.post.image,
                'caption': talent.post.caption,
                'created_at': talent.post.created_at,
                'updated_at': talent.post.updated_at,
                'status': talent.post.status,
                'no_of_likes': talent.post.no_of_likes,
                'month': talent.month,
                'year': talent.year,
            }
            print(f"post_data: {post_data}")
            final_posts.append(post_data)
        profile = Profile.objects.get(user=request.user)
        context={
            'post':final_posts,
            'profile':profile
        }
        return render(request, 'talents.html',context)
    else:
        invalid="Not Authorized"
        return render(request, 'loginn.html',{'invalid':invalid})