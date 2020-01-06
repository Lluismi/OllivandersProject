# casos test
from main import *


def test_aged_brie():
    aged = AgedBrie('AgedBrie', 2, 0)
    assert aged.sell_in == 2
    aged.update_quality()
    assert aged.quality == 1


def test_normal_item():
    elixir = NormalItem('Elixir of the Moongose', 5, 7)
    assert elixir.quality == 7
    elixir.set_sellIn()
    assert elixir.sell_in == 4


def test_sulfuras():
    sulfuras = Sulfuras('Sulfuras, Hand of Ragnaros', 0, 80)
    sulfuras.set_sellIn()
    sulfuras.update_quality()
    assert sulfuras.sell_in == 0
    assert sulfuras.quality == 80
