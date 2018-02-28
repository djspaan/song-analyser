class Mapper:
    YEAR_COLUMN = 'year'
    ARTIST_COLUMN = 'artist'
    TITLE_COLUMN = 'title'
    LYRICS_COLUMN = 'lyrics'

    reader = None

    def __init__(self, reader):
        self.reader = reader

    def map(self):
        pass
