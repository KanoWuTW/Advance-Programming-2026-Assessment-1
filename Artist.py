class Artist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add_song(self, song_name):
        self.__songs.append(song_name)
