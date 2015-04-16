class AbstractOrder(object):

    def __init__(self, qty)
        self.base_price = base_price

    def base_price(self):
        return 5.00

class WaterAbstractOrderOrder(AbstractOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        total = self.base_price() * qty
        
        if qty >= 3:
            total = total * 0.75

        if self.imported:
            total = total * 1.5
            
        return total

class CantalopeOrder(AbstractOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        total = self.base_price() * qty
        if qty >= 5:
            total = total * 0.5

        return total

class CasabaOrder(AbstractOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    
    def get_price(self, qty):
        total = (self.base_price() + 1) * 1.5 * qty

        return total


class SharlynOrder(AbstractOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        return total


class Santa_ClausOrder(AbstractOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        return total

class ChristmasOrder(AbstractOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        total = self.base_price() * qty
        return total

class Horned_AbstractOrderOrder(AbstractOrder):
    species = 'Horned AbstractOrder'
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        return total


class XiguaOrder(AbstractOrder):
    species = 'Xigua'
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5 * 2) * qty
        return total


class OgenOrder(AbstractOrder):
    species = 'Ogen'
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        total = (self.base_price() + 1) * qty
        return total