from containers import SongCollection


class SongStore:
    songs = []

    def __init__(self, songs=[]):
        self.songs = songs

    def add(self, song):
        self.songs.append(song)

    def all(self):
        return SongCollection(self.songs)

    def where(self, key, value):
        return SongStore(self.songs).where(key, value)

    def __getitem__(self, key):
        return self.songs[key]

    def __str__(self):
        return '\n'.join(map(str, self.songs))
