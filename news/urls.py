from django.urls import path
from news import views


urlpatterns = [
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<str:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
]
