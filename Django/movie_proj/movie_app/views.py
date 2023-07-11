from django.shortcuts import render, get_object_or_404
from django.db.models import F
# Create your views here.
from .models import Movie, Director, Actor


def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_first=True), 'rating')
    # movies = Movie.objects.order_by('rating', '-year')
    # agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        # 'agg': agg,
        # 'total': movies.count()
    })


def show_one_movie(request, id_movie: int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/directors.html', {
        'directors': directors
    })

def show_director(request, dir:int):
    director = get_object_or_404(Director, id=dir)
    return render(request, 'movie_app/director.html',{
        'director': director
    })

def show_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {
        'actors': actors
    })

def show_actor(request, act:int):
    actor = get_object_or_404(Actor, id=act)
    return render(request, 'movie_app/actor.html',{
        'actor': actor
    })
