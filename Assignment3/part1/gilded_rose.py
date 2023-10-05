# -*- coding: utf-8 -*-

class Item:
    DEFAULT_ADJUSTMENT = 1

    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    # Printing off item info when item is printed 
    def __repr__(self):
        return "%s, %s, %s," % (self.name, self.sell_in, self.quality)
    def update_quality_amount(self):
        pass
    def sell_in_adjustment(self):
        pass    
    def negative_quality_check(self):
        if self.quality <= 0:
            self.quality = 0
            return 0
    def max_quality_check(self):
        DEFAULT_MAX_QUALITY = 50
        if self.quality >= DEFAULT_MAX_QUALITY:
            self.quality = DEFAULT_MAX_QUALITY
            return 0
        
    def past_sell_by_date(self):
        if self.sell_in <= 1:
            return True
        else:
            return False
    
    
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
    def update_quality_amount(self):

        adjustment = 0


	    # - The Quality of an item is never negative
        if super().negative_quality_check() == 0:
            return 0   
        # - The Quality of an item is never more than 50
        if super().max_quality_check() == 0:
            return 0
        # checking to see if past sell by date
        past_sell_by_date = super().past_sell_by_date()
        
	    # - "Aged Brie" actually increases in Quality the older it gets
        if past_sell_by_date:
            adjustment = Item.DEFAULT_ADJUSTMENT * 2
            return adjustment 
        else:
            adjustment = Item.DEFAULT_ADJUSTMENT
            return adjustment
    def sell_in_adjustment(self):
        Item.DEFAULT_ADJUSTMENT = 1
        return -Item.DEFAULT_ADJUSTMENT



class BackstagePass(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality_amount(self):

        adjustment = 0


	    # - The Quality of an item is never negative
        if super().negative_quality_check() == 0:
            return 0   


        # - The Quality of an item is never more than 50
        if super().max_quality_check() == 0:
            return 0

        # checking to see if past sell by date
        past_sell_by_date = super().past_sell_by_date()
        
        # - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        # Quality drops to 0 after the concert
        if self.sell_in >5 and self.sell_in <= 10:
            adjustment = Item.DEFAULT_ADJUSTMENT * 2
            return adjustment
        elif self.sell_in <= 5:
            adjustment = Item.DEFAULT_ADJUSTMENT * 3
            return adjustment
        elif past_sell_by_date:
            self.quality = 0
            return 0
        else:
            adjustment = Item.DEFAULT_ADJUSTMENT
            return adjustment
        
    def sell_in_adjustment(self):
        Item.DEFAULT_ADJUSTMENT = 1
        return -Item.DEFAULT_ADJUSTMENT

class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    # - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def update_quality_amount(self):
        return 0 
    def sell_in_adjustment(self):
        return 0
    

class Conjured(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality_amount(self):

        adjustment = 0

	    # - The Quality of an item is never negative
        if super().negative_quality_check() == 0:
            return 0   


        # - The Quality of an item is never more than 50
        if super().max_quality_check() == 0:
            return 0
        
        # checking to see if past sell by date
        past_sell_by_date = super().past_sell_by_date()

        
        # - "Conjured" items degrade in Quality twice as fast as normal items
        adjustment = -Item.DEFAULT_ADJUSTMENT * 2
        return adjustment
    def sell_in_adjustment(self):
        DEFAULT_ADJUSTMENT = 1
        return -DEFAULT_ADJUSTMENT

class Normal(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
    
    def update_quality_amount(self):

        adjustment = 0

        past_sell_by_date = False

	    # - The Quality of an item is never negative
        if super().negative_quality_check() == 0:
            return 0   


        # - The Quality of an item is never more than 50
        if super().max_quality_check() == 0:
            return 0
        
        # checking to see if past sell by date
        past_sell_by_date = super().past_sell_by_date()
    
        if past_sell_by_date:
            adjustment = -Item.DEFAULT_ADJUSTMENT * 2
            return adjustment
        else:
            adjustment = -Item.DEFAULT_ADJUSTMENT
            return adjustment
    

    def sell_in_adjustment(self):
        DEFAULT_ADJUSTMENT = 1
        return -DEFAULT_ADJUSTMENT
    

class GildedRose(object):

    SULFURAS = "Sulfuras"
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes"
    CONJURED = "Conjured"
    NORMAL = "normal"


    # Mapping the item type to the class to instantiate later
    item_type_to_class = {
        SULFURAS: Sulfuras,
        AGED_BRIE: AgedBrie,
        BACKSTAGE_PASS: BackstagePass,
        CONJURED: Conjured,
        NORMAL: Normal
    }


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
                return self.NORMAL
            

    def update_quality(self):
        print("Updating quality method called")
        # Let's use the iterator design pattern to loop through the list
        it = iter(self.items)
        # for item in self.items:
        for item in it:
            
            # First get the type of each item 
            print(item.__repr__())
            item_type = self.get_item_type(item.name)

            # Method for determining how much the quality should be increased or decreased
            itemClass = self.item_type_to_class.get(item_type)
            newObject = itemClass(item.name, item.sell_in, item.quality)
            quality_adjustment_amount = newObject.update_quality_amount()

            print(f"The item type is: {item_type}")
            print((f"The adjustment is {quality_adjustment_amount}"))
            # Added to handle edge cases
            if item.quality + quality_adjustment_amount >=50 and item_type != self.SULFURAS:
                item.quality = 50
            else:
                item.quality += quality_adjustment_amount

            # Method for determining how much the sell in date should be decreased by
            sell_in_adjustment_amount_ = newObject.sell_in_adjustment()
            item.sell_in += sell_in_adjustment_amount_
            print("The sell in amount is : ", sell_in_adjustment_amount_)
            print("\n")


def main():
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]   
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    print("\n")
    gilded_rose.update_quality()
    print("\n")

    gilded_rose.update_quality()

    

if __name__ == "__main__":
    main()
