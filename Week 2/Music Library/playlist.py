import json


class Playlist():

    @staticmethod
    def load(file_name):
        filename = "{}".format(file_name)
        my_json_file = open(filename, 'r')
        content = my_json_file.read()
        my_json_file.close()
        return content

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        flag = False
        while not flag:
            n = 0
            for song in self.songs:
                if song.title == song_name:
                    n += 1
                    self.songs.remove(song)
                    break
            if n == 0:
                flag = True

    def total_length(self):
        result = 0
        for song in self.songs:
            result += song.length
        return result

    def remove_disrated(self, rating):
        flag = False
        while not flag:
            n = 0
            for song in self.songs:
                if song.rating <= rating:
                    n += 1
                    self.songs.remove(song)
                    break
            if n == 0:
                flag = True

    def remove_bad_quality(self):
        flag = False
        while not flag:
            n = 0
            for song in self.songs:
                if song.bitrate < 200:
                    n += 1
                    self.songs.remove(song)
                    break
            if n == 0:
                flag = True

    def show_artists(self):
        result = []
        for song in self.songs:
            is_in_list = False
            for artist_in_result in result:
                if song.artist == artist_in_result:
                    is_in_list = True
            if not is_in_list:
                result.append(song.artist)
        return result

    def __str__(self):
        result = ""
        for song in self.songs:
            song_min = song.length // 60
            song_sec = song.length - song_min * 60
            if song_min < 10 and song_sec > 10:
                result += "{} {} - 0{}:{}'\n'".format(song.artist, song.title, song_min, song_sec)
            elif song_min > 10 and song_sec < 10:
                result += "{} {} - {}:0{}'\n'".format(song.artist, song.title, song_min, song_sec)
            elif song_min < 10 and song_sec < 10:
                result += "{} {} - 0{}:0{}'\n'".format(song.artist, song.title, song_min, song_sec)
            else:
                result += "{} {} - {}:{}'\n'".format(song.artist, song.title, song_min, song_sec)
        result = result[:len(result) - 3]
        return result

    def save(self, file_name):
        song_arr = []
        for song in self.songs:
            #"title": song.title, "artist": song.artist,
                #"album": song.album, "rating": song.rating, "length": song.length,
                #"bitrate": song.bitrate
            temp_song = song.__dict__
            song_arr.append(temp_song)
        new_playlist = {"name": self.name, "songs": song_arr}
        new_playlist = json.dumps(new_playlist)

        big_file = open(file_name, 'w')
        big_file.write("".join(new_playlist))
        big_file.close()
