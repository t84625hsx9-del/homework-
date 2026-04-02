from .views import UserUpdateView, UserCreateView, UserDetailView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', UserCreateView.as_view(), name='signup'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='profile_detail'),
    path('<int:pk>/', UserDetailView.as_view(), name='profile_edit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]