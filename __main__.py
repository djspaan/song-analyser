from readers import CSVReader
from mappers import SongMapper
from stores import SongStore


# from models import Song


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        mapper = SongMapper(CSVReader())
        store = SongStore()
        mapper.map_to_store(store)

        print(store)

if __name__ == '__main__':
    Main.run()
