import threading

from ..exceptionsUtils import UnavailableIngredientException



class Machine:
    '''
    numberOfOutlets is the number of beverages our machine can produce simultaneously
    inventory is a Map of Ingredients and their available portions
    '''

    def __init__(self, numberOfOutlets, inventory,beverageMaker):
        self.numberOfOutlets = numberOfOutlets
        self.inventory = inventory
        self.beverageMaker = beverageMaker
        self.currentOrders = 0
        self.totalBeveragesBrewed = 0
        #self._lock = threading.Lock()

    '''
    A refill method that updates the quantity of an
    existing ingredient or adds a new ingredient to the inventory
    '''



    def make_beverage(self, beverage):

        if self.currentOrders == self.numberOfOutlets:
            print ("No outlets available")
            return False

        self.currentOrders += 1

        '''
                Now Brew the beverage and update Ingredient 
                in the Inventory by locking it        
        '''

        result = self.beverageMaker.brew(inventory=self.inventory, beverageToBrew=beverage)
       # print(result)
        if not("because" in result):
            self.totalBeveragesBrewed += 1

        print(result)
        self.currentOrders -= 1



#        print(result ,"is brewed")

        #return True
