import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story", "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc ", "some tagline", "a date")

# print toy_story.storyline

avatar = movie.Movie("Avatar", "https://resizing.flixster.com/wmwaS9C76fnLpML3UAj0i3l6djw=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDU0OzEyMDA7ODAwOzEyMDA", "https://www.youtube.com/watch?v=cRdxXPV9GNQ", "some tagline", "a date")

# print avatar.storyline

# avatar.show_trailer()

alien = movie.Movie("Alien", "https://fanart.tv/fanart/movies/348/movieposter/alien-527cde786d68c.jpg", "https://www.youtube.com/watch?v=LjLamj-b0I8", "some tagline", "a date")

# alien.show_trailer()

lalaland = movie.Movie("La La Land", "http://www.impawards.com/2016/posters/la_la_land_ver8.jpg", "https://www.youtube.com/watch?v=0pdqf4P9MB8", "some tagline", "a date")

mortal_kombat = movie.Movie("Mortal Kombat", "http://cdn.sockshare.net/bUYVUiY.png", "https://www.youtube.com/watch?v=6LxGtUWxv0o", "some tagline", "a date")

rocky = movie.Movie("Rocky", "https://ctcmr.files.wordpress.com/2010/12/image-php.jpeg", "https://www.youtube.com/watch?v=7RYpJAUMo2M", "some tagline", "a date")

# movies = [toy_story, avatar, alien, lalaland, mortal_kombat, rocky ]

avatar.get_storyline()
avatar.get_release_date()
print lalaland.movie_id
# fresh_tomatoes.open_movies_page(movies)

# print media.Movie.__doc__python 