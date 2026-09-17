from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('journal/', views.journal, name='journal'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mood-history/', views.mood_history, name='mood_history'),
    path('wellness-analysis/', views.wellness_analysis, name='wellness_analysis'),
    path('wellness-activities/',views.wellness_activities,name='wellness_activities'),
    path('profile/', views.profile, name='profile'),
]