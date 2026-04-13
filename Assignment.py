import os
import time



class Artist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add_song(self, song_name):
        self.__songs.append(song_name)


class Song:
    number_of_songs = 0

    def __init__(self, title, duration, genre, artist=None):
        self.title = title
        if not isinstance(duration, int):
            raise TypeError("duration must be integer.")
        self.duration = duration
        self.genre = genre
        Song.number_of_songs += 1
        self.id = self.number_of_songs
        if artist != None:
            artist.add_song(self.title)
            self.artist = artist


class StreamService:
    def __init__(self):
        self.options = {
            "1": "Search songs by title.",
            "2": "Search songs by artists.",
            "3": "Browse all songs.",
        }
        self.songs = []
        self.__add_new_song(Song("Hello world", 180, "Pop", Artist("Kevin")))
        self.__add_new_song(Song("Hello world", 160, "Classic", Artist("Thea")))

    def __add_new_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def __main_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to music streaming service!")
        for k, v in self.options.items():
            print(f"{k}. {v}")

    def __formatted_print_song(self, song):
        print(f"{song.title} by {song.artist.name}")

    def __player(self, song_id):
        # song = self.find_song_by_id(song_id)
        # time_elapsed = 0
        # played_time = 0
        # self.start()
        # while played_time < song.duration:
        #     time_elapsed = time_elapsed + self.re_get_time()
        #     while time_elapsed >= 1:
        #         played_time += 1
        #         time_elapsed -= 1
        #         # os.system("cls" if os.name == "nt" else "clear")
        #         print(played_time)
        song = self.find_song_by_id(song_id)

        start_time = time.perf_counter()
        last_shown = 0

        while last_shown < song.duration:
            current = int(time.perf_counter() - start_time)

            if current > last_shown:
                last_shown = current
                print(last_shown)

    def __find_song(self, artist=None, keyword=None):
        result = {}
        index = 1
        for s in self.songs:
            if artist == None:
                if s.title == keyword:
                    result[index] = s
                    index += 1
            else:
                if s.title == keyword and s.artist.name == artist:
                    result[index] = s
                    index += 1

        return result

    def find_song_by_id(self, id):
        for s in self.songs:
            if s.id == id:
                return s

    def __songs_by_title(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Search by title.")
        title = input("Title: ")
        result = self.__find_song(keyword=title)
        if result == {}:
            print("Sorry, not matching songs has been found.")
            selection = input("Press any key to return.")
            return
        else:
            for i in range(1, len(result) + 1):
                print(i, end=". ")
                self.__formatted_print_song(result[i])
            selection = input("Select one song to play or press 'r' to return.")

        song = result.get(int(selection))
        self.__player(song.id)

    def run_service(self):
        while True:
            self.__main_menu()
            while True:
                try:
                    i = int(input(""))
                    break
                except:
                    print("Please enter valid input!")
            actions = list(self.options.keys())
            action = actions[i - 1]

            if action == "1":
                self.__songs_by_title()
            elif action == "2":
                pass
            elif action == "3":
                pass


ss = StreamService()
ss.run_service()
