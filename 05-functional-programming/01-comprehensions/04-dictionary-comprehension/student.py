def title_to_director(movies):
    return{movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    return{movie_y.director: [movie_x.title for movie_x in movies if movie_y.director == movie_x.director] for movie_y in movies}