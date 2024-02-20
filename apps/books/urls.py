from django.urls import path

from apps.books import views

urlpatterns = [
    path('lists/', views.BooksListAPIView.as_view()),
    path('create/', views.BookCreateAPIView.as_view()),
    path('update/<int:pk>/', views.BookUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.BookDeleteAPIView.as_view()),
]
