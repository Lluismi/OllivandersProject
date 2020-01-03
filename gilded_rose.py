# -*- coding: utf-8 -*-
from Updateable import Updateable
from NormalItem import NormalItem
from AgedBrie import AgedBrie
from BackstagePass import BackstagePass
from Conjured import Conjured
from Sulfuras import Sulfuras


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def get_items(self):

        reader = open(self.items, "r")
        lines = reader.read().rstrip()
        return lines

    def update_quality():
        self.items.update_quality()


if __name__ == '__main__':
    objetos = GildedRose("stdout.gr")
    print(objetos.get_items())
