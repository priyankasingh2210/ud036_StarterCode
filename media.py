import webbrowser


class Movie():
    """
    title,storyline,poster image and movie trailer url as constructor params
    """
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_trailer_url):
        # instance variables
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.movie_poster_image = movie_poster_image
        self.movie_trailer_url = movie_trailer_url

    # a method which would open webrowser and launch movie instance trailer
    def show_trailer(self):
        webbrowser.open(self.movie_trailer_url)
