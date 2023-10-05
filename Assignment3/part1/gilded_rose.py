# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    # Printing off item info when item is printed 
    def __repr__(self):
        return "%s, %s, %s," % (self.name, self.sell_in, self.quality)
    
class Iterable(object):
    def __init__(self, items):
        self.items = items
        self.index = 0
    def __iter__(self):
        # Returns the iterator object itself
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
class AgedBrie(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1
class BackstagePass(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality += 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    def update_quality(self):
        pass
class Conjured(Item):
    # def __init__(self, name, sell_in, quality):
    #     super().__init__(name, sell_in, quality)
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 2
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 2
class Normal(Item):
    # def __init__(self, name, sell_in, quality):
    #     super().__init__(name, sell_in, quality)
    def update_quality(self):
        if self.quality > 0:
            self.quality -= 1
        self.sell_in -= 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality -= 1
    

class GildedRose(object):

    SULFURAS = "Sulfuras"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes"
    CONJURED = "Conjured"

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    # Looping through the list. Ideally we would have a hashmap for O(1) lookup
    def get_item_sell_in(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.sell_in

    def get_item_quality(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item.quality
            
    def get_item_type (self, item_name):
            if "backstage passe" in item_name.lower():
                return self.BACKSTAGE_PASS
            elif "aged brie" in item_name.lower():
                return self.AGED_BRIE
            elif "sulfuras" in item_name.lower():
                return self.SULFURAS
            elif "conjured" in item_name.lower():
                return self.CONJURED
            else:
                return "normal"
            
    def quality_adjustment(self, item: Item, item_type):


        DEFAULT_MAX_QUALITY = 50
        DEFAULT_ADJUSTMENT = 1

        adjustment = 0


        # Determine if the item has passed the sell by date
    	# - Once the sell by date has passed, Quality degrades twice as fast
        past_sell_by_date = False
        if item.sell_in <= 1:
            past_sell_by_date = True

	    # - The Quality of an item is never negative
        if item.quality <= 0:
            item.quality = 0
            return 0

        # - The Quality of an item is never more than 50
        if item_type != self.SULFURAS and item.quality >= DEFAULT_MAX_QUALITY:
            item.quality = DEFAULT_MAX_QUALITY
            return 0


	    # - "Aged Brie" actually increases in Quality the older it gets
        if item_type == self.AGED_BRIE:
            if past_sell_by_date:
                adjustment = DEFAULT_ADJUSTMENT * 2
                return adjustment 
            else:
                adjustment = DEFAULT_ADJUSTMENT
                return adjustment
        # - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        # Quality drops to 0 after the concert
        elif item_type == self.BACKSTAGE_PASS:
            if item.sell_in >5 and item.sell_in <= 10:
                adjustment = DEFAULT_ADJUSTMENT * 2
                return adjustment
            elif item.sell_in <= 5:
                adjustment = DEFAULT_ADJUSTMENT * 3
                return adjustment
            elif past_sell_by_date:
                item.quality = 0
                return 0
            else:
                adjustment = DEFAULT_ADJUSTMENT
                return adjustment
        # - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        elif item_type == self.SULFURAS:
            adjustment = 0
            return adjustment
        # - "Conjured" items degrade in Quality twice as fast as normal items
        elif item_type == self.CONJURED:
            adjustment = -DEFAULT_ADJUSTMENT * 2
            return adjustment
        else:
            if past_sell_by_date:
                adjustment = -DEFAULT_ADJUSTMENT * 2
                return adjustment
            else:
                adjustment = -DEFAULT_ADJUSTMENT
                return adjustment

            
    def sell_in_adjustment(self, item: Item, item_name):
        DEFAULT_ADJUSTMENT = 1
        if item_name == self.SULFURAS:
            return 0
        else:
            return -DEFAULT_ADJUSTMENT


    def update_quality(self):
        print("Updating quality method called")
        # Let's use the iterator design pattern to loop through the list
        it = iter(self.items)
        # for item in self.items:
        for item in it:
            
            # First get the type of each item 
            print(item.__repr__())
            item_type = self.get_item_type(item.name)
            print(f"The item type is: ", item_type)   

            # Method for determining how much the quality should be increased or decreased
            quality_adjustment_amount = self.quality_adjustment(item, item_type)
            print(f"The adjustment is: ", quality_adjustment_amount)
            # Added to handle edge cases
            if item.quality + quality_adjustment_amount >=50 and item_type != self.SULFURAS:
                item.quality = 50
            else:
                item.quality += quality_adjustment_amount

            # Method for determining how much the sell in date should be decreased by
            sell_in_adjustment_amount = self.sell_in_adjustment(item, item_type)
            item.sell_in += sell_in_adjustment_amount

            # # Checking a full backstage name but should be backstage in the name
            # if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            #     # Making sure item quality does not go below 0
            #     if item.quality > 0:
            #         if item.name != "Sulfuras, Hand of Ragnaros":
            #             item.quality = item.quality - 1
            # else:
            #     if item.quality < 50:
            #         # Increasing item quality the first time 
            #         item.quality = item.quality + 1
            #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #             if item.sell_in < 11:
            #                 if item.quality < 50:
            #                     # Increasing item quality the second time
            #                     item.quality = item.quality + 1
            #             if item.sell_in < 6:
            #                 if item.quality < 50:
            #                     # Increasing item quality the second time
            #                     item.quality = item.quality + 1
            # # Checking full sulfuras name but should be sulfuras in the name
            # # Sulfuras does not change sell in date
            # if item.name != "Sulfuras, Hand of Ragnaros":
            #     item.sell_in = item.sell_in - 1
            
            # # Item has passed sell by date
            # if item.sell_in < 0:
            #     if item.name != "Aged Brie":
            #         if item.name != "Backstage passes to a TAFKAL80ETC concert":
            #             if item.quality > 0:
            #                 if item.name != "Sulfuras, Hand of Ragnaros":
            #                     item.quality = item.quality - 1
            #         else:
            #             item.quality = item.quality - item.quality
            #     else:
            #         if item.quality < 50:
            #             item.quality = item.quality + 1

# def main():
#     items = [
#              Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
#              Item(name="Aged Brie", sell_in=2, quality=0),
#              Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
#              Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
#              Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
#              Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
#              Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
#             ]   
#     gilded_rose = GildedRose(items)
#     gilded_rose.update_quality()
#     print("\n")
#     gilded_rose.update_quality()
#     print("\n")

#     gilded_rose.update_quality()

    

# if __name__ == "__main__":
#     main()
