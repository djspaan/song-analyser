from csv import reader


class CSVSongReader:
    source = ''
    header = []
    songs = []

    def __init__(self, song_file):
        self.source = song_file
        self.read_from_file()

    def read_from_file(self):
        songs = open(self.source, "r")
        lines = list(reader(songs))
        self.header = lines.pop(0)
        self.songs = lines

    def get_column_index(self, name):
        print(self.header)
        return self.header.index(name)

    def get_column_items(self, index):
        return [song[index] for song in self.songs]

    def get_items(self, column_name):
        column_index = self.get_column_index(column_name)
        return self.get_column_items(column_index)
