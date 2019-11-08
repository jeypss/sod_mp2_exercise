class Property:
    def __init__(self, sqm: int, bdr: int, btr: int, is_furnished: bool):
        self.sqm = sqm
        self.bdr = bdr
        self.btr = btr
        self.is_furnished = is_furnished

    def add(self):
        pass

    def update(self):
        pass

    def view(self):
        pass

class House(Property):
    def __init__(self, sqm, bdr, btr, is_furnished, stories, with_yard, with_garage):
        super().__init__(sqm, bdr, btr, is_furnished)
        self.stories = stories
        self.with_yard = with_yard
        self.with_garage = with_garage

class Apartment(Property):
    def __init__(self, sqm, bdr, btr, is_furnished, with_laundry):
        super().__init__(sqm, bdr, btr, is_furnished)
        self.with_laundry = with_laundry

class Rental:
    def __init__(self, rent, frequency):
        self.rent = rent
        self.frequency = frequency

class Purchase:
    def __init__(self, purchase_price):
        self.purchase_price = purchase_price

class HouseRental(House, Rental):
    pass

class HousePurchase(House, Purchase):
    pass

class AptRental(Apartment, Rental):
    pass

class AptPurchase(Apartment, Purchase):
    pass
