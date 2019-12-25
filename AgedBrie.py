# Clase para los items AgedBrie

from NormalItem import NormalItem


class AgedBrie(NormalItem):

    def update_quality(self):
        self.quality += 1


if __name__ == '__main__':
    Brie = AgedBrie('AgedBrie', 20, 33)
    print(Brie.sell_in, Brie.quality)
    Brie.update_quality()
    Brie.set_sellIn()
    print(Brie.sell_in, Brie.quality)
