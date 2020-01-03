# Archivo principal
from NormalItem import NormalItem
from AgedBrie import AgedBrie
# Crear los objetos de las clases con el archivo


def class_objects(items):
    try:
        if 'Aged' in items[0]:
            aged_item = AgedBrie(items[0], items[1], items[2])
            print(aged_item)
            return aged_item
        else:
            normal_item = NormalItem(items[0], items[1], items[2])
            print(normal_item)
            return normal_item
    except IndexError:
        pass


def create_objects():
    reader = open('stdout.gr', 'r')
    for i, lines in enumerate(reader):
        if i in range(2, 11):
            lines = reader.readline()
            print(lines)
            lines = lines.split(',')
            # print(lines)
            # class_objects(lines)


if __name__ == '__main__':
    create_objects()
