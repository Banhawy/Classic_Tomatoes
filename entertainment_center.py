import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story")

avatar = movie.Movie("Avatar")

alien = movie.Movie("Alien")

lalaland = movie.Movie("La La Land")

mortal_kombat = movie.Movie("Mortal Kombat")

rocky = movie.Movie("Rocky")

godfather = movie.Movie("The Godfather")

green_mile = movie.Movie("The Green Mile")

pulp_fiction = movie.Movie("Pulp Fiction")

movies = [toy_story, avatar, alien, lalaland, mortal_kombat, rocky, godfather, green_mile, pulp_fiction ]

# avatar.get_storyline()
# avatar.get_release_date()
# # print lalaland.movie_id
# print avatar.trailer_youtube_url
# lalaland.show_trailer()
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.__doc__python 