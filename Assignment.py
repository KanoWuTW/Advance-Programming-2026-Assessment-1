import os
import time
import keyboard
import json


class Artist:
    def __init__(self, name):
        self.name = name
        self.__songs = []

    def add_song(self, song_name):
        self.__songs.append(song_name)


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


class StreamService:
    def __init__(self):
        self.options = {
            "1": "Search songs by title.",
            "2": "Search songs by artists.",
            "3": "Browse all songs.",
        }
        self.songs = []
        self.artists = []
        self.__load_songs()

    def __load_songs(self):
        with open("songs.json", "r") as file:
            data = json.load(file)
        for song in data:
            singer = None
            if song["artist"] != None:
                creatd = False
                for a in self.artists:
                    if a.name == song["artist"]:
                        a.add_song(song["title"])
                        creatd = True
                        singer = a
                        break
                if creatd == False:
                    artist = Artist(song["artist"])
                    artist.add_song(song["title"])
                    self.artists.append(artist)
                    singer = artist

            self.__add_new_song(Song(song, singer))

    def __add_new_song(self, song):
        self.songs.append(song)

    def __main_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to music streaming service!")
        for k, v in self.options.items():
            print(f"{k}. {v}")

    def __get_formatted_songname(self, song):
        name = None
        if song.artist.name == "":
            name = "anonymous"
        else:
            name = song.artist.name
        return f"{song.title} by {name}"

    def __get_formatted_playetime(self, time_played):
        s = time_played % 60
        m = (time_played // 60) % 60
        h = (time_played // 60) // 60

        if s < 10:
            s = "0" + str(s)
        if m < 10:
            m = "0" + str(m)
        if h < 10:
            h = "0" + str(h)

        return f"{h}, {m}, {s}"

    def __player(self, song_id):
        song = self.find_song_by_id(song_id)
        time_played = 0
        last_shown = time.perf_counter()
        while True:
            time_elapsed = time.perf_counter() - last_shown
            while time_elapsed >= 1:
                time_elapsed -= 1
                last_shown = time.perf_counter()
                time_played += 1
                os.system("cls" if os.name == "nt" else "clear")
                print(f"You are now listening {self.__get_formatted_songname(song)}.")
                print(
                    f"{self.__get_formatted_playetime(time_played)} / {self.__get_formatted_playetime(song.duration)}"
                )
                print("Press q to stop playing.")
            if keyboard.is_pressed("q"):
                break
            if time_played > song.duration:
                break

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

    def __list_all_songs(self):
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(1, len(self.songs) + 1):
            print(i, end=". ")
            print(self.__get_formatted_songname(self.songs[i - 1]))
        input("")

    def view_all_artists(self):
        os.system("cls" if os.name == "nt" else "clear")
        index = 1
        for i in self.artists:
            print(f"{index}. {i.name}")
            index += 1

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
                print(self.__get_formatted_songname(result[i]))

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
                self.__list_all_songs()
            elif action == "4":
                pass


ss = StreamService()
ss.view_all_artists()
