class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Updatable():

    def update_quality(self):
        pass


class NormalItem(Item, Updatable):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)