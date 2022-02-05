from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('feedback/', views.FeedBackUs, name='FeedBackUs'),
    # path('ViewMember/<int:accid>', views.viewMember, name='Members'),
    path('ViewMember/', views.viewMember, name='Members'),
    path('login/', views.loginFEAT, name='loginUser')
    ]


# urlpatterns = [
#     path('login/', views.login_view, name='login_view'),
#     path('register/', views.register, name='register'),
#     path('adminpage/', views.admin, name='adminpage'),
#     path('customer/', views.customer, name='customer'),
#     path('employee/', views.employee, name='employee'),
# ]