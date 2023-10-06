class Item:

    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

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
    DEFAULT_ADJUSTMENT = 1

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality_amount(self):

        adjustment = 0

        # - The Quality of an item is never negative
        if self.quality < 0:
            self.quality = 0
            return 0
        # - The Quality of an item is never more than 50
        DEFAULT_MAX_QUALITY = 50
        if self.quality >= DEFAULT_MAX_QUALITY:
            self.quality = DEFAULT_MAX_QUALITY
            return 0
        # checking to see if past sell by date
        past_sell_by_date = False

        if self.sell_in <= 0:
            past_sell_by_date = True
        else:
            past_sell_by_date =  False

        # - "Aged Brie" actually increases in Quality the older it gets
        if past_sell_by_date:
            adjustment = self.DEFAULT_ADJUSTMENT * 2
            return adjustment
        else:
            adjustment = self.DEFAULT_ADJUSTMENT
            return adjustment

    def sell_in_adjustment(self):
        Item.DEFAULT_ADJUSTMENT = 1
        return -self.DEFAULT_ADJUSTMENT


class BackstagePass(Item):
    DEFAULT_ADJUSTMENT = 1
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality_amount(self):

        adjustment = 0

        # - The Quality of an item is never negative
        if self.quality < 0:
            self.quality = 0
            return 0

        # - The Quality of an item is never more than 50
        DEFAULT_MAX_QUALITY = 50
        if self.quality >= DEFAULT_MAX_QUALITY:
            self.quality = DEFAULT_MAX_QUALITY
            return 0

        # checking to see if past sell by date
        past_sell_by_date = False

        if self.sell_in <= 0:
            past_sell_by_date = True
        else:
            past_sell_by_date =  False
        # - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
        # Quality drops to 0 after the concert
        if self.sell_in > 5 and self.sell_in <= 10:
            adjustment = self.DEFAULT_ADJUSTMENT * 2
            return adjustment
        elif self.sell_in <= 5:
            adjustment = self.DEFAULT_ADJUSTMENT * 3
            return adjustment
        elif past_sell_by_date:
            self.quality = 0
            return 0
        else:
            adjustment = self.DEFAULT_ADJUSTMENT
            return adjustment

    def sell_in_adjustment(self):
        self.DEFAULT_ADJUSTMENT = 1
        return -self.DEFAULT_ADJUSTMENT


class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    # - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def update_quality_amount(self):
        return 0

    def sell_in_adjustment(self):
        return 0


class Conjured(Item):
    DEFAULT_ADJUSTMENT = 1

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality_amount(self):

        adjustment = 0

        # - The Quality of an item is never negative
        if self.quality < 0:
            self.quality = 0
            return 0

        # - The Quality of an item is never more than 50
        DEFAULT_MAX_QUALITY = 50
        if self.quality >= DEFAULT_MAX_QUALITY:
            self.quality = DEFAULT_MAX_QUALITY
            return 0

        # checking to see if past sell by date
        past_sell_by_date = False

        if self.sell_in <= 0:
            past_sell_by_date = True
        else:
            past_sell_by_date =  False
        # - "Conjured" items degrade in Quality twice as fast as normal items
        adjustment = -self.DEFAULT_ADJUSTMENT * 2
        return adjustment

    def sell_in_adjustment(self):
        DEFAULT_ADJUSTMENT = 1
        return -DEFAULT_ADJUSTMENT


class Normal(Item):
    DEFAULT_ADJUSTMENT = 1

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality_amount(self):

        adjustment = 0

        past_sell_by_date = False

        # - The Quality of an item is never negative
        if self.quality < 0:
            self.quality = 0
            return 0

        # - The Quality of an item is never more than 50
        DEFAULT_MAX_QUALITY = 50
        if self.quality >= DEFAULT_MAX_QUALITY:
            self.quality = DEFAULT_MAX_QUALITY
            return 0

        # checking to see if past sell by date
        past_sell_by_date = False

        if self.sell_in <= 0:
            past_sell_by_date = True
        else:
            past_sell_by_date =  False

        if past_sell_by_date and self.quality >= 2:
            adjustment = -self.DEFAULT_ADJUSTMENT * 2
            return adjustment
        else:
            if self.quality >= 1:
                adjustment = -self.DEFAULT_ADJUSTMENT
                return adjustment
            else:
                return 0

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

    def get_item_type(self, item_name):
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
        # Let's use the iterator design pattern to loop through the list
        it = iter(self.items)
        for item in it:

            # First get the type of each item
            item_type = self.get_item_type(item.name)

            # Method for determining how much the quality should be increased or decreased
            itemClass = self.item_type_to_class.get(item_type)
            newObject = itemClass(item.name, item.sell_in, item.quality)
            quality_adjustment_amount = newObject.update_quality_amount()

            # Method for determining how much the sell in date should be decreased by
            sell_in_adjustment_amount_ = newObject.sell_in_adjustment()
            item.sell_in += sell_in_adjustment_amount_

            # Added to handle edge cases
            if item.quality + quality_adjustment_amount < 0 or item.quality < 0:
                item.quality = 0
            elif item_type in "Backstage passes" and item.sell_in <= 0:
                item.quality = 0
            elif item.quality + quality_adjustment_amount >= 50 and item_type != self.SULFURAS:
                item.quality = 50
            else:
                item.quality += quality_adjustment_amount
