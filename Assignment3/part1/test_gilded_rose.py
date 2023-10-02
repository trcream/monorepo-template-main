# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

# unittesting the GildedRose class

class GildedRoseTest(unittest.TestCase):
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
        assert gr.get_item_sell_in("test3") == 9
        assert gr.get_item_quality("test3") == 9
        

    # - Once the sell by date has passed, Quality degrades twice as fast
    def test_sell_by_date_passed(self):
        # Arrange
        items = [Item("test4",0,10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("test4") == -1
        assert gr.get_item_quality("test4") == 8
        
	# - The Quality of an item is never negative
    def test_negative_quality(self):
        # Assert
        items = [Item("test5",5,0)]
        gr = GildedRose(items)

        # Act 
        gr.update_quality()

        # Testing that the quality does not go below 0
        assert gr.get_item_quality("test5") == 0



	# - "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie(self):
        # Arrange
        items = [Item("Aged Brie",5,10)]

        # Act
        gr = GildedRose(items)
        gr.update_quality()

        # Assert 
        # As the days go by the quality increases
        assert gr.get_item_sell_in("Aged Brie") == 4
        assert gr.get_item_quality("Aged Brie") == 11

	# - The Quality of an item is never more than 50
    def test_max_quality(self):
        # Arrange
        items = [Item("Aged Brie",5,49), Item("Aged Brie of France",5,49)]
        # Act 
        gr = GildedRose(items)
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Aged Brie") == 4
        assert gr.get_item_quality("Aged Brie") == 50, f"Expected quality to be 50 quality is {gr.get_item_quality('Aged Brie')}"

        assert gr.get_item_sell_in("Aged Brie of France") == 4
        assert gr.get_item_quality("Aged Brie of France") == 50, f"Expected quality to be 50 quality is {gr.get_item_quality('Aged Brie of France')}"

        # Act
        gr.update_quality()

        # Assert 
        assert gr.get_item_sell_in("Aged Brie") == 3
        assert gr.get_item_quality("Aged Brie") == 50, f"Expected quality to be 50 quality is {gr.get_item_quality('Aged Brie')}"


	# - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    # Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
    # legendary item and as such its Quality is 80 and it never alters.
    def test_sulfuras(self):
        # Arrange
        items= [Item("Sulfuras, Hand of Ragnaros", 5, 80), Item("Sulfuras, Arm of Ragnaros", 5, 80)]

        # Act
        gr = GildedRose(items)
        gr.update_quality()

        # Assert
        assert gr.get_item_sell_in("Sulfuras, Hand of Ragnaros") == 5
        assert gr.get_item_quality("Sulfuras, Hand of Ragnaros") == 80

        assert gr.get_item_sell_in("Sulfuras, Arm of Ragnaros") == 5
        assert gr.get_item_quality("Sulfuras, Arm of Ragnaros") == 80


	# - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
	# Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
	# Quality drops to 0 after the concert

    def test_backstage_passes(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20),
                 Item("Backstage passes to the best concert ever", 20, 30)]

        # Act 
        gr = GildedRose(items)
        gr.update_quality()

        # Assert 
        # Increase in quality as sell in date approaches
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 10
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 21

        assert gr.get_item_sell_in("Backstage passes to the best concert ever") == 19
        assert gr.get_item_quality("Backstage passes to the best concert ever") == 31

	    # Quality increases by 2 when there are 10 days or less
        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 9
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 23

        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 8
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 25

        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 7
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 27

        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 6
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 29

        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 5
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 31

        # Quality increase by 3 when there are 5 days or less
        gr.update_quality()
        assert gr.get_item_sell_in("Backstage passes to a TAFKAL80ETC concert") == 4
        assert gr.get_item_quality("Backstage passes to a TAFKAL80ETC concert") == 34


    
        
    # Conjured is not updating at all we need to implement 
    # "Conjured" items degrade in Quality twice as fast as normal items
    def test_conjured_item(self):
        # Arrange
        items = [Item("Conjured", 5, 42)]
        gr = GildedRose(items)

        original_sell_in = gr.get_item_sell_in("Conjured")
        original_quality = gr.get_item_quality("Conjured")
        print(f"Original sell in days is {original_sell_in}")
        print(f"Original quality is {original_quality}")


        # Act
        gr.update_quality()

        print(f"Updated sell in days is {original_sell_in}")
        print(f"Updated quality is {original_quality}")

        # Assert
        new_sell_in = gr.get_item_sell_in("Conjured")
        new_quality = gr.get_item_quality("Conjured")



        assert new_sell_in < original_sell_in
        assert new_sell_in == original_sell_in - 1

        assert new_quality > -1
        assert new_quality <= 50
        assert new_quality < original_quality
        assert new_quality == original_quality - 2


if __name__ == '__main__':
    unittest.main()
