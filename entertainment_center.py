import movie
import classic_tomatoes

# Add the names of the movies to be displayed on the page to this list
movie_list = [
    "Groundhog Day", "Alien", "The Godfather 2",
    "Mortal Kombat", "Rocky", "La La Land",
    "The Green Mile", "Pulp Fiction", "Forrest Gump"
]

movies = []

# Loop instantiates each movie name in the movie_list into a movie class object
# and appends it into a new list movies[]
for film in movie_list:
    movies.append(movie.Movie(film))

# Pass the movie object list to the html python template
classic_tomatoes.open_movies_page(movies)

