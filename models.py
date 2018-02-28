# TODO: Implement
# class Artist:
#     name = ''
#     songs = []
#
#     def __init__(self, name='', songs=[]):
#         self.name = name
#         self.songs = songs


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

    def __str__(self):
        return "%s | %s - %s" % (self.year, self.artist, self.title)
