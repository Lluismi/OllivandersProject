# Clase Sulfuras

from NormalItem import NormalItem


class Sulfuras(NormalItem):

    def set_sellIn(self):
        self.sell_in = 0

    def update_quality(self):
        self.sell_in = self.sell_in


if __name__ == "__main__":
    Sulfuro = Sulfuras('Sulfuras, lasjd', 20, 23)
    print(Sulfuro.sell_in, Sulfuro.quality)
    Sulfuro.set_sellIn()
    Sulfuro.update_quality()
    print(Sulfuro.sell_in, Sulfuro.quality)
