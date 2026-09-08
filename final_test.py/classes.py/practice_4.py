# Create a Playlist class holding a list of song titles; add add_song, remove_song, and
# shuffle_order (rotating the list is fine — no random needed).
class Playlist :
    def __init__(self, song_titles):
        self.song_titles = song_titles

    def add_song(self, song) :
        self.song_titles.append(song)
        return self.song_titles

    def remove_song(self, song) :
        if song in self.song_titles :
            self.song_titles.remove(song)
        else :
            return False

    def shuffle_order(self) :
        a = self.song_titles[1:]
        b = self.song_titles[:1]
        return a + b

