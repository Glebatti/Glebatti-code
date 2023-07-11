from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('16/', views.get_info_about_16),
    path('', views.index, name='horoscope-index'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name')
]