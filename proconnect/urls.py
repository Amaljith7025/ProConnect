from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', views.home, name='home'),
    path('base', views.base, name='base'),
    path('signin', views.signIn, name='signin'),
    path('signup', views.signup, name='signup'),
    path('', views.landingpage, name='landingpage'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/complete/google-oauth2/', views.google_oauth2_complete, name='google_oauth2_complete'),
    path('complete_profile/', views.complete_profile, name='complete_profile')
]
