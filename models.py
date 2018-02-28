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
        limited = {k: str(v)[:20] for k, v in self.__dict__.iteritems()}
        return str(limited)
