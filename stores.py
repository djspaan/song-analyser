class SongStore:
    songs = []

    def __init__(self):
        pass

    def add(self, song):
        self.songs.append(song)

    def get_all(self):
        return self.songs

    def __str__(self):
        return ' ---- '.join(map(str, self.songs))



