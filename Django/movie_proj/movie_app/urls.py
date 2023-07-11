from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<int:id_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_directors),
    path('directors/<int:dir>', views.show_director, name='director-detail'),
    path('actors/', views.show_actors),
    path('actors/<int:act>', views.show_actor, name='actor-detail'),
]
