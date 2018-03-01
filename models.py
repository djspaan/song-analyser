# TODO: Implement
# class Artist:
#     name = ''
#     songs = []
#
#     def __init__(self, name='', songs=[]):
#         self.name = name
#         self.songs = songs


class Song:
    def __init__(self, **kwargs):
        for key in kwargs:
            self.__dict__[key] = kwargs[key]

    def __str__(self):
        limited = {key: str(value)[:20] for key, value in self.__dict__.iteritems()}
        return str(limited)
