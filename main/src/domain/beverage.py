import threading

'''Pure Data Class'''
class Beverage:
    '''
    composition is a dict/Map of ingredient and quantity
    '''

    def __init__(self, name, composition):
        self.name = name
        self.composition = composition

    '''
    
    YAGNI
       a method that ascertains if a beverage can be
       prepared
    

    def isBrewable(self, inventory):
        if len(inventory) == 0:
            print("Inventory is exhausted, refill now !")
            return False

        for ingredient, value in self.composition.items():
            if ingredient not in inventory:
                print(self.name, "cannot be prepared because %s is not available" % ingredient)
                return False
            elif inventory[ingredient] < value:
                print(self.name, "cannot be prepared because %s is not sufficient" % ingredient)
                return False
        return True
        
    '''
