from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('feedback/', views.FeedBackUs, name='FeedBackUs'),
    path('ViewMember/', views.viewMember, name='Members'),
    path('login/', views.loginFEAT, name='loginUser')
]
