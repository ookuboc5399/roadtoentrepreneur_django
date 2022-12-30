from django.urls import path
from stock import views


urlpatterns = [
    path('stock/', views.StockView.as_view(), name='stock'),
    path('stock/<str:pk>/', views.StockDetailView.as_view(), name='stock-detail'),
    path('serch_stock/', views.StockSearchView.as_view(), name='stock-search'),

]

