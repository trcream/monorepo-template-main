# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

# unittesting the GildedRose class

class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    # 	- All items have a SellIn value which denotes the number of days we have to sell the item

    def test_get_item_sell_in(self):
        # Arrange
        items = [Item("test1",5,6)]
        gr = GildedRose(items)
        assert items[0].sell_in == gr.get_item_sell_in("test1")
    # All items have a Quality value which denotes how valuable the item is
    def test_get_item_quality(self):
        # Arrange
        items = [Item("test2",4,8)]
        gr = GildedRose(items)
        assert items[0].quality == gr.get_item_quality("test2")

    # At the end of each day our system lowers both values for every item
    def test_lower_quality_quantity(self):
        # Arrange
        items = [Item("test3",10,10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert items[0].quality == 9
        assert items[0].sell_in == 9
        

    # - Once the sell by date has passed, Quality degrades twice as fast
	# - The Quality of an item is never negative
	# - "Aged Brie" actually increases in Quality the older it gets
	# - The Quality of an item is never more than 50
	# - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
	# - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
	# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	# Quality drops to 0 after the concert

    
        
    # Conjured is not updating at all
    # "Conjured" items degrade in Quality twice as fast as normal items
    # def test_conjured_item(self):
    #     # Arrange
    #     items = [Item("Conjured", 5, 42)]
    #     gr = GildedRose(items)

    #     original_sell_in = gr.get_item_sell_in("Conjured")
    #     original_quality = gr.get_item_quality("Conjured")
    #     print(f"Original sell in days is {original_sell_in}")
    #     print(f"Original quality is {original_quality}")


    #     # Act
    #     gr.update_quality()

    #     print(f"Updated sell in days is {original_sell_in}")
    #     print(f"Updated quality is {original_quality}")

    #     # Assert
    #     new_sell_in = gr.get_item_sell_in("Conjured")
    #     new_quality = gr.get_item_quality("Conjured")



    #     assert new_sell_in < original_sell_in
    #     assert new_sell_in == original_sell_in - 1

    #     assert new_quality > -1
    #     assert new_quality <= 50
    #     assert new_quality < original_quality
    #     assert new_quality == original_quality - 2


if __name__ == '__main__':
    unittest.main()
