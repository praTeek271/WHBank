from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('feedback/', views.FeedBackUs, name='FeedBackUs'),
    path('ViewMember/', views.viewMember, name='Members'),
    path('customer/<int:acc>', views.Member, name='ViewMemberdetails'),
    path('transacton_history/<str:user>', views.transaction_log, name='ViewMemberTransactionLog'),
    
]


