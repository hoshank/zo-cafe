import threading


class Machine:
    '''
    numberOfOutlets is the number of beverages our machine can produce simultaneously
    inventory is a Map of Ingredients and their available portions
    '''

    def __init__(self, numberOfOutlets, inventory):
        self.numberOfOutlets = numberOfOutlets
        self.inventory = inventory
        self.currentOrders = 0
        self._lock = threading.Lock()

    '''
    A refill method that updates the quantity of an
    existing ingredient or adds a new ingredient to the inventory
    '''

    def refill(self,ingredient,quantity):
        if ingredient in self.inventory:
            self.inventory[ingredient] += quantity
            print("Quantity of %s" % ingredient ,"has been updated in inventory by %s" % quantity)
        else:
            self.inventory[ingredient] = quantity
            print("Ingredient %s" % ingredient ,"has been added in inventory with quantity of %s" % quantity)


    def make_beverage(self, beverage):

        if self.currentOrders == self.numberOfOutlets:
            print ("No outlets available")
            return False

        self.currentOrders += 1

        ingredients_needed = beverage.composition

        self._lock.acquire()
        result = beverage.canPrepareBeverage(self.inventory)

        if not result:
            self._lock.release()
            self.currentOrders -= 1
            return result

        for ingredient, value in ingredients_needed.items():
            self.inventory[ingredient] -= value

        self._lock.release()
        self.currentOrders -= 1

        print("%s is prepared" % beverage.name)

        return True
