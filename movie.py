import media
import requests

class Movie(media.Media):
    """"This class stores Movie related information"""
    def __init__(self, title, poster_image, trailer_youtube, tagline, release_date):
        media.Media.__init__(self, title, poster_image, trailer_youtube)
        self.tagline = tagline
        self.release_date = release_date

    def get_tagline(self):
        self.movie_id
        query_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + "?language=en-US&api_key=873c09566ed2be62fbd02102e48c399e"
        details = requests.get(query_api_url).json()
        self.tagline = details["tagline"]
        print self.tagline

    def get_release_date(self):
        self.movie_id
        query_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + "?language=en-US&api_key=873c09566ed2be62fbd02102e48c399e"
        details = requests.get(query_api_url).json()
        self.release_date = details["release_date"]
        print self.release_date
