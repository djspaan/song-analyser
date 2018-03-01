from csv import reader


class CSVReader:
    source_file = ''

    def __init__(self, source_file):
        self.source_file = source_file

    @staticmethod
    def parse_items(header, rows):
        items = []
        for row in rows:
            item = {}
            for i, column in enumerate(header):
                item[column] = row[i]
            items.append(item)
        return items

    def get_items(self):
        items = open(self.source_file, "r")
        rows = list(reader(items))
        header = rows.pop(0)
        return CSVReader.parse_items(header, rows)