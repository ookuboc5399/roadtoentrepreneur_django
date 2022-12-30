from django.urls import path
from books import views

urlpatterns = [
    path("book/", views.BookView.as_view(), name='book'),
    path('book/<str:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]