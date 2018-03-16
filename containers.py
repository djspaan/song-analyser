class Collection:
    items = []

    def __init__(self, items=[]):
        self.items = items

    def all(self):
        return self.items

    def count(self):
        return len(self.items)

    def pluck(self, attribute):
        return [getattr(item, attribute) for item in self.items]

    def first(self):
        return self.items[0]

    def take(self, amount):
        return Collection(self.items[0:amount])

    def map(self, callback):
        return {item.Title: callback(item) for item in self.items}

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
