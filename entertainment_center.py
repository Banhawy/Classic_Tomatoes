import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story", """http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/
toy_story_wallpaper_by_artifypics-d5gss19.jpg""")

avatar = movie.Movie("Avatar", """https://resizing.flixster.com/wmwaS9C76fnLpML3UAj0i3l6djw=/206x30
5/v1.bTsxMTE3Njc5MjtqOzE3NDU0OzEyMDA7ODAwOzEyMDA""")

alien = movie.Movie("Alien", """https://fanart.tv/fanart/movies/348/movieposter/alien-527cde786d68c.
jpg""")

lalaland = movie.Movie("La La Land", "http://www.impawards.com/2016/posters/la_la_land_ver8.jpg")

mortal_kombat = movie.Movie("Mortal Kombat", "http://cdn.sockshare.net/bUYVUiY.png")

rocky = movie.Movie("Rocky", "https://ctcmr.files.wordpress.com/2010/12/image-php.jpeg")

movies = [toy_story, avatar, alien, lalaland, mortal_kombat, rocky ]

# avatar.get_storyline()
# avatar.get_release_date()
# # print lalaland.movie_id
# print avatar.trailer_youtube_url
# lalaland.show_trailer()
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.__doc__python 