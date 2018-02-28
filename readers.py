from csv import reader


class CSVReader:
    def __init__(self):
        pass

    @staticmethod
    def parse_items(header, rows):
        items = []
        for row in rows:
            item = {}
            for i, column in enumerate(header):
                item[column] = row[i]
            items.append(item)
        return items

    @staticmethod
    def get_items(source_file):
        items = open(source_file, "r")
        rows = list(reader(items))
        header = rows.pop(0)
        return CSVReader.parse_items(header, rows)