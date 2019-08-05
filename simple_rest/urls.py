from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views
from .views import home
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('languages/', include('languages.urls')),
    path('api-url/', include('rest_framework.urls')),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGIN_REDIRECT_URL), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('social/', include('social_app.urls'))
]