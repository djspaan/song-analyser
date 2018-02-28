class Collection:
    items = []

    def __init__(self, items=[]):
        self.items = items

    def all(self):
        return self.items

    def __getitem__(self, key):
        return self.items[key]

    def __str__(self):
        return '\n'.join(map(str, self.items))


class SongCollection(Collection):
    def __init__(self, items=None):
        Collection.__init__(self, items)

    def where(self, key, value):
        items = [item for item in self.items if getattr(item, key) == value]
        return SongCollection(items)
