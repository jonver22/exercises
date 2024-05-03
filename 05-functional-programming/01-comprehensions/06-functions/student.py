def movie_count(movies, director):
    return len([movie.title for movie in movies if movie.director == director])