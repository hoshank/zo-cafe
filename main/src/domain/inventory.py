from ..exceptionsUtils.InsufficientIngredientException import InsufficientIngredientException
from ..exceptionsUtils.UnavailableIngredientException import UnavailableIngredientException

import threading

class Inventory:
    def __init__(self,inventory):
        self.inventory = inventory
        self._inventoryLock = threading.Lock()

    def refill(self, ingredient, quantity):
        self._inventoryLock.acquire()
        if ingredient in self.inventory:
            self.inventory[ingredient] += quantity
            print("Quantity of {} has been updated in inventory by {}".format(ingredient, quantity))
        else:
            self.inventory[ingredient] = quantity
            print("Ingredient {} has been added in inventory with quantity of {}".format(ingredient, quantity))
        self._inventoryLock.release()


    def consume(self, ingredient, quantity):
        self._inventoryLock.acquire()

        # if len(self.inventory) == 0:
        #     print("Inventory is exhausted, refill now !")
        #     raise UnavailableIngredientException()

        if ingredient not in self.inventory:
            #print("{} ingredient is not Available".format(ingredient) )
            self._inventoryLock.release()
            raise UnavailableIngredientException()

        if self.inventory[ingredient] < quantity:
            #print("{} ingredient is not sufficient".format(ingredient) )
            self._inventoryLock.release()
            raise InsufficientIngredientException()

        self.inventory[ingredient] -= quantity

        if self.inventory[ingredient] < 10:
            print(ingredient, " is running low")

        self._inventoryLock.release()

