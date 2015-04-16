class Melon(object):
    def base_price(self):
        return 5.00

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        total = self.base_price() * qty
        if qty >= 3:
            total = total * 0.75
        print total

class CantalopeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        total = self.base_price() * qty
        if qty >= 5:
            total = total * 0.5

        print total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    
    def get_price(self, qty):
        total = (self.base_price() + 1) * 1.5 * qty

        print total


class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        print total


class Santa_ClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        print total

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        total = self.base_price() * qty
        print total

class Horned_MelonOrder(Melon):
    species = 'Horned Melon'
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5) * qty
        print total


class XiguaOrder(Melon):
    species = 'Xigua'
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        total = (self.base_price() * 1.5 * 2) * qty
        print total


class OgenOrder(Melon):
    species = 'Ogen'
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        total = (self.base_price() + 1) * qty
        print total