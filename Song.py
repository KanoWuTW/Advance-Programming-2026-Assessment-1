class Song:
    number_of_songs = 0

    def __init__(self, song, artist):
        self.title = song["title"]
        self.duration = song["duration"]
        self.genre = song["genre"]
        self.avg_rating = song["avg_rating"]
        self.rating_num = song["rating_num"]
        Song.number_of_songs += 1
        self.id = self.number_of_songs
        self.artist = artist

    def to_dict(self):
        return {
            "title": self.title,
            "duration": self.duration,
            "genre": self.genre,
            "rating_num": self.rating_num,
            "avg_rating": self.avg_rating if self.avg_rating is not None else "N/A",
            "artist": self.artist.name if self.artist else None,
        }
