from models import Song


class SongMapper:
    SONG_FILE = './songdata.csv'

    reader = None

    def __init__(self, reader):
        self.reader = reader

    def map_to_store(self, store):
        for song in self.reader.get_items(self.SONG_FILE):
            store.add(Song(**song))
        return store
