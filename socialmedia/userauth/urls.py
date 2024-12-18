from django.contrib import admin
from django.urls import path
from socialmedia import settings
from userauth import views,admin_views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('loginn/',views.loginn),
    path('signup/',views.signup),
    path('logoutt/',views.logoutt),
    path('upload',views.upload),
    path('rates/<str:id>', views.rates, name='rates'),
    path('allow/<str:id>', views.allow, name='allow'),
    path('deny/<str:id>', views.deny, name='deny'),
    path('#<str:id>', views.home_post),
    path('explore',views.explore),
    path('denied',admin_views.denied),
    path('profile/<str:id_user>', views.profile),
    path('delete/<str:id>', views.delete),
    path('search-results/', views.search_results, name='search_results'),
    path('follow', views.follow, name='follow'),
    path('month-talent', admin_views.talent_of_the_month, name='talent_of_the_month'),
    path('talents', admin_views.talents),    
    
]
