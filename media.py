import webbrowser
import json
import requests
 
class  Media():
    """ This class provides a way of storing media related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title):
        self.title = title

        # API call to get movie_id which is used in subsequent API calls
        self.api_url = """https://api.themoviedb.org/3/search/movie?api_key=873c09566ed2be62fbd02102
        e48c399e&query=""" + self.title
        self.data = requests.get(self.api_url).json()
        self.movie_id = self.data["results"][0]["id"]

        # GET media poster and concatentate to poster URL
        self.poster_path = self.data["results"][0]["poster_path"]
        self.poster_image_url = "http://image.tmdb.org/t/p/w500/" + self.poster_path

        # Api call to get media's youtube trailer key
        self.youtube_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + "/vid" \
        "eos?language=en-US&api_key=873c09566ed2be62fbd02102e48c399e"
        self.data2 = requests.get(self.youtube_api_url).json()
        try:
            self.youtube_key = self.data2["results"][0]["key"]
            # Get the youtube key of type Trailer
            for i in range(len(self.data2["results"])):
                if self.data2["results"][i]["type"] == "Trailer":
                    self.youtube_key = self.data2["results"][i]["key"]
                    break
        except IndexError:
            # If json object doesn't contain trailer or is empty returns a "Coming Soon" video
            print  self.title + " needs to be uploaded manually"
            self.youtube_key = "0TjxnrWT8Es"
        self.trailer_youtube_url = "www.youtube.com/watch?v=" + self.youtube_key




    def get_storyline(self):
        query_api_url = "https://api.themoviedb.org/3/movie/" + str(self.movie_id) + """?language=
        en-US&api_key=873c09566ed2be62fbd02102e48c399e"""
        details = requests.get(query_api_url).json()
        self.storyline = details["overview"]
        # print self.storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    # def get_poster(self):
 