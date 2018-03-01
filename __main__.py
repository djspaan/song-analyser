from readers import CSVReader
from mappers import SongMapper
from stores import SongStore

SONG_FILE = './data/songdata.csv'


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        mapper = SongMapper(CSVReader(SONG_FILE))
        store = mapper.map_to_store(SongStore())
        print(store.all())


if __name__ == '__main__':
    Main.run()
