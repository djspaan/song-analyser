from readers import CSVReader
from mappers import SongMapper
from stores import SongStore


class Main:
    def __init__(self):
        pass

    @staticmethod
    def run():
        mapper = SongMapper(CSVReader())
        store = mapper.map_to_store(SongStore())
        print(store.where('artist', 'Candyman').where('year', '1990'))


if __name__ == '__main__':
    Main.run()
