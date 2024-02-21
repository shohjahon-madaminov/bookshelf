from django.urls import path

from apps.users import views

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogOutAPIView.as_view()),
    path('refresh/token/', views.LoginRefreshAPIVIew.as_view()),
    path('profile/<str:username>/', views.UserProfileAPIView.as_view()),
]
