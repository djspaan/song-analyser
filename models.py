class Song:
    year = None
    artist = ''
    title = ''
    lyrics = ''

    def __init__(self, year=None, artist='', title='', lyrics=''):
        self.year = year
        self.artist = artist
        self.title = title
        self.lyrics = lyrics
