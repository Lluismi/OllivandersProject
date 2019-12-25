# Clase NormalItem, hereda de Updateable e Item
# será la base para casi todos los items de la tienda.

from Item import Item
from Updateable import Updateable


class NormalItem(Item, Updateable):

    def set_sellIn(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.quality >= 0 and self.quality <= 50:
            self.quality -= 1
