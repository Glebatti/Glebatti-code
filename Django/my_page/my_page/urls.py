"""my_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from horoscope import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('16/', views.get_info_about_16),
    # path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    # path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac),
    path('horoscope/', include('horoscope.urls')),
    # path('horoscope/type', include('horoscope.urls')),

]
