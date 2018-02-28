class SongStore:
    songs = []

    def __init__(self, songs=[]):
        self.songs = songs

    def add(self, song):
        self.songs.append(song)

    def all(self):
        return self.songs

    def where(self, key, value):
        songs = [song for song in self.songs if getattr(song, key) == value]
        return SongStore(songs)

    def __getitem__(self, key):
        return self.songs[key]

    def __str__(self):
        return '\n'.join(map(str, self.songs))



