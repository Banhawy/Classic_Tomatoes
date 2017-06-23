import media
import requests

class Movie(media.Media):
    """"This class stores Movie related information"""
    def __init__(self, title):
        media.Media.__init__(self, title)

        # GET Movie tagline
        self.query_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + """?langua
        ge=en-US&api_key=873c09566ed2be62fbd02102e48c399e"""
        self.details = requests.get(self.query_api_url).json()
        self.tagline = self.details["tagline"]

        # GET movie release date
        self.release_date = self.details["release_date"]
