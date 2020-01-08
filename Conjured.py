# Clase para los nuevo tipos de objeto Conjured

from NormalItem import NormalItem


class Conjured(NormalItem):

    def update_quality(self):
        if self.quality > 0:
            self.quality -= 2
        else:
            self.quality -= 4


if __name__ == '__main__':
    cake = Conjured('Conjured Mana Cake', 3, 6)
    print(cake.sell_in, cake.quality)
    cake.set_sellIn()
    cake.update_quality()
    print(cake.sell_in, cake.quality)
