from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programing/', include('programing.urls')),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('news/', include('news.urls')),
    path('stock/', include('stock.urls')),
    path('authen/', include('djoser.urls.jwt')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/verify/', TokenVerifyView.as_view()),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('app.urls')),
    path('api1/', include('books.urls')),
    path('api2/', include('news.urls')),
    path('api3/', include('stock.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
