import webbrowser
import json
import requests
 
class  Media():
    """ This class provides a way of storing media related information"""

    VALID_RATINGS = [ "G", "PG",  "PG-13", "R"]
    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.api_url = "https://api.themoviedb.org/3/search/movie?api_key=873c09566ed2be62fbd02102e48c399e&query=" + self.title
        self.data = requests.get(self.api_url).json()
        self.movie_id = self.data["results"][0]["id"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_storyline(self):
        self.movie_id
        query_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + "?language=en-US&api_key=873c09566ed2be62fbd02102e48c399e"
        details = requests.get(query_api_url).json()
        self.storyline = details["overview"]
        print self.storyline
        
    # def get_poster(self):
 