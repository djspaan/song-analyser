from readers import CSVSongReader
# from mappers import Mapper
# from models import Song


class Main:
    SONG_FILE = './songdata.csv'

    def __init__(self):
        pass

    def run(self):
        file_reader = CSVSongReader(self.SONG_FILE)
        print(file_reader.get_items('artist'))


if __name__ == '__main__':
    main = Main()
    main.run()
