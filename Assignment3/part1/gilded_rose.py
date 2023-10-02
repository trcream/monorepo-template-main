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
    

class GildedRose(object):

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
                return "backstage"
            elif "aged brie" in item_name.lower():
                return "aged brie"
            elif "sulfuras" in item_name.lower():
                return "sulfuras"
            elif "conjured" in item_name.lower():
                return "conjured"
            else:
                return "normal"




    def update_quality(self):
        print("Updating quality method called")
        # Let's use the iterator design pattern to loop through the list
        it = iter(self.items)
        # for item in self.items:
        for item in it:
            
            # First get the type of each item 
            item_type = self.get_item_type(item.name)
            print(f"The item type is: ", item_type)   
            print(item.__repr__())

            # Method for determining how much the quality should be increased or decreased

            # Method for determining how much the sell in date should be decreased by

            # Checking a full backstage name but should be backstage in the name
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                # Making sure item quality does not go below 0
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    # Increasing item quality the first time 
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                # Increasing item quality the second time
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                # Increasing item quality the second time
                                item.quality = item.quality + 1
            # Checking full sulfuras name but should be sulfuras in the name
            # Sulfuras does not change sell in date
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            
            # Item has passed sell by date
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1

    

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
    gilded_rose.update_quality()
    gilded_rose.update_quality()

    

if __name__ == "__main__":
    main()
