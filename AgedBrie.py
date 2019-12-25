# Clase para los items AgedBrie

from NormalItem import NormalItem


class AgedBrie(NormalItem):

    def update_quality(self):
        self.quality += 1
