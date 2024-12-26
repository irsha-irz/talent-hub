from itertools import chain
from django.shortcuts  import  get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import  Followers, PostRatings, Post, Profile
from django.db.models import Q
from django.utils import timezone
from django.db.models import Sum
from .models import TalentOfTheMonth



def signup(request):
 try:
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('emailid')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        my_user=User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        if my_user is not None:
            login(request,my_user)
            return redirect('/')
        return redirect('/loginn')
    
        
 except:
        invalid="User already exists"
        return render(request, 'signup.html',{'invalid':invalid})
  
    
 return render(request, 'signup.html')   
    

def loginn(request):
 
  if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/')
        
 
        invalid="Invalid Credentials"
        return render(request, 'loginn.html',{'invalid':invalid})
               
  return render(request, 'loginn.html')

@login_required(login_url='/loginn')
def logoutt(request):
    logout(request)
    return redirect('/loginn')



@login_required(login_url='/loginn')
def home(request):
    user = User.objects.filter(username=request.user.username).first()
    final_posts = []
    if (user.is_superuser == True):
        final_posts = Post.objects.filter(status__in=["ALLOWED", "PENDING"]).order_by('-created_at', '-updated_at')
    else:
        posts = Post.objects.filter(Q(status="ALLOWED")).order_by('-updated_at').all()
        post_ids = posts.values_list('id', flat=True)
        print(f"post_ids: {post_ids}")
        likes = PostRatings.objects.filter(Q (post_id__in=post_ids)).all()
        #print(f"likes: {likes}")
        likes_dict = {like.post_id: like.ratings for like in likes}
        print(f"likes_dict: {likes_dict}")
        current_month = timezone.now().month
        current_year = timezone.now().year
        talent = TalentOfTheMonth.objects.filter(Q (post__in=posts, month=current_month,year=current_year)).first()
        #print(f"talent: {talent.post}")
        for post in posts:
            post_data = {
                'id': post.id,
                'user': post.user,
                'image': post.image,
                'caption': post.caption,
                'created_at': post.created_at,
                'updated_at': post.updated_at,
                'status': post.status,
                'no_of_likes': post.no_of_likes,
                'rates': likes_dict.get(post.id, 0),
                'talent': 1 if talent and (talent.post == post) else 0,
            }
            print(f"post_data: {post_data}")
            final_posts.append(post_data)

    profile = Profile.objects.get(user=request.user)

    context = {
        'post': final_posts,
        'profile': profile,
    }
    
    print(f"user: {user}, isAdmin: {user.is_superuser}")

    if (user.is_superuser == True):
        return render(request, 'admin_main.html',context)
    return render(request, 'main.html',context)
    


@login_required(login_url='/loginn')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/loginn')
def rates(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id)
        count = request.GET.get('rating', '0')        
        rating = int(count)
        like_filter = PostRatings.objects.filter(post_id=id, username=username).first()

        if like_filter is None:
            new_like = PostRatings.objects.create(post_id=id, username=username, ratings=rating)
            post.no_of_likes = post.no_of_likes + rating
        else:
            old_rating = like_filter.ratings
            like_filter.ratings = rating
            like_filter.save()
            post.no_of_likes = post.no_of_likes - old_rating + rating

        post.save()

        # Generate the URL for the current post's detail page
        print(post.id)

        # Redirect back to the post's detail page
        return redirect('/#'+id)
    
@login_required(login_url='/loginn')
#@permission_required(perm="adminstrator")
def allow(request, id):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        if (user.is_superuser == True):
            post = get_object_or_404(Post, id=id)
            post.status = "ALLOWED"
            post.save()
            print(post.id)
            # Redirect back to the post's detail page
            return redirect('/#'+id)
        else:
            print("User is not an admin")
            invalid="Not Authorized"
            return render(request, 'loginn.html',{'invalid':invalid}) 

@login_required(login_url='/loginn')
def deny(request, id):
    if request.method == 'GET':
        user = User.objects.filter(username=request.user.username).first()
        if (user.is_superuser == True):
            post = get_object_or_404(Post, id=id)
            post.status = "DENIED"
            post.save()
            print(post.id)
            # Redirect back to the post's detail page
            return redirect('/#'+id)
        else:
            print("User is not an admin")
            invalid="Not Authorized"
            return render(request, 'loginn.html',{'invalid':invalid}) 

@login_required(login_url='/loginn')
def explore(request):
    post=Post.objects.filter(status="ALLOWED").order_by('-created_at')
    profile = Profile.objects.get(user=request.user)

    context={
        'post':post,
        'profile':profile
        
    }
    return render(request, 'explore.html',context)

@login_required(login_url='/loginn')
def profile(request,id_user):
    user_object = User.objects.get(username=id_user)
    print(user_object)
    profile = Profile.objects.get(user=request.user)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=id_user).order_by('-created_at')
    user_post_length = len(user_posts)

    follower = request.user.username
    user = id_user
    
    if Followers.objects.filter(follower=follower, user=user).first():
        follow_unfollow = 'Unfollow'
    else:
        follow_unfollow = 'Follow'

    user_followers = len(Followers.objects.filter(user=id_user))
    user_following = len(Followers.objects.filter(follower=id_user))

    context = {
        'user_object': user_object,
        'is_admin': user_object.is_superuser,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'profile': profile,
        'follow_unfollow':follow_unfollow,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    
    
    if request.user.username == id_user:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
             image = user_profile.profileimg
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            if request.FILES.get('image') != None:
             image = request.FILES.get('image')
             bio = request.POST['bio']
             location = request.POST['location']

             user_profile.profileimg = image
             user_profile.bio = bio
             user_profile.location = location
             user_profile.save()
            

            return redirect('/profile/'+id_user)
        else:
            return render(request, 'profile.html', context)
    return render(request, 'profile.html', context)

@login_required(login_url='/loginn')
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/profile/'+ request.user.username)


@login_required(login_url='/loginn')
def search_results(request):
    query = request.GET.get('q')

    users = Profile.objects.filter(user__username__icontains=query)
    posts = Post.objects.filter(caption__icontains=query)
    print(f"users: {users}, posts: {posts}")
    context = {
        'query': query,
        'users': users,
        'posts': posts,
    }
    return render(request, 'search_user.html', context)

def home_post(request,id):
    post=Post.objects.get(id=id)
    profile = Profile.objects.get(user=request.user)
    context={
        'post':post,
        'profile':profile
    }
    return render(request, 'main.html',context)



def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Followers.objects.filter(follower=follower, user=user).first():
            delete_follower = Followers.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = Followers.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')
