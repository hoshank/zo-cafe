from ..exceptionsUtils.InsufficientIngredientException import InsufficientIngredientException
from ..exceptionsUtils.UnavailableIngredientException import UnavailableIngredientException

class BeverageMaker:
    def __init__(self):
        pass
    '''
    def __init__(self, beverages):
        self.beverages = beverages

    def add_beverage(self, beverage):
        self.beverages.append(beverage)
    '''

    def brew(self, inventory, beverageToBrew):
        successMessage = "{} is prepared".format(beverageToBrew.name)
        failureMessagePrefix = "{} cannot be prepared because".format(beverageToBrew.name)
        for ingredient in beverageToBrew.composition:
            try:
                inventory.consume(ingredient, beverageToBrew.composition[ingredient])
            except UnavailableIngredientException :
                return "{} {} is not available".format(failureMessagePrefix, ingredient)
            except InsufficientIngredientException:
                return "{} item {} is not sufficient".format(failureMessagePrefix, ingredient)
        return successMessage
