from main.src.domain.machine import Machine
from main.src.domain.beverage import Beverage

from resources.test.decorators.testDecorator import testDecorator

'''
all tests written first to ensure Red, Green and Refactor

Used Decorator to display method name and result before it is executed
'''

def setupOneOutletMachineWithNoInventory():
    return Machine(1,{})

basicMilkInventory = 1000
basicWaterInventory = 1000
basicCocoaInventory = 200
basicTeaSyrupInventory = 100

def setupOneOutletMachineWithBasicInventory():
    return Machine(1,{"milk": basicMilkInventory,
                    "water":basicWaterInventory,
                    "cocoa": basicCocoaInventory,
                    "tea_syrup": basicTeaSyrupInventory})

def setupBlackTea():
    return Beverage("black tea",{"water": 200, "tea_syrup": 10})

@testDecorator
def refillCanAddNewIngredientsIfNotPresent():
   # arrange
    machineUnderTest = setupOneOutletMachineWithNoInventory()
    #act
    machineUnderTest.refill("cocoa",100)
   #assert
    assert len(machineUnderTest.inventory) == 1
    assert machineUnderTest.inventory["cocoa"] == 100

@testDecorator
def refillCanUpdateIngredientQuantityIfPresent():
   # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    #act
    itemQuantityToUpdate = 100
    itemUnderTest = "cocoa"
    machineUnderTest.refill(itemUnderTest, itemQuantityToUpdate)
   #assert
    assert machineUnderTest.inventory["cocoa"] == basicCocoaInventory + itemQuantityToUpdate
    assert machineUnderTest.inventory["milk"] == basicMilkInventory

@testDecorator
def canMakeOneBeverageIfIngredientsPresentInInventory():
    # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    beverageUnderTest = Beverage("black tea",{"water": 200, "tea_syrup": 10})
    # act
    machineUnderTest.make_beverage(beverageUnderTest)
    # assert
    assert machineUnderTest.inventory["tea_syrup"] == basicTeaSyrupInventory - beverageUnderTest.composition["tea_syrup"]
    assert machineUnderTest.inventory["water"] == basicWaterInventory - beverageUnderTest.composition["water"]

@testDecorator
def canMakeTwoBeverageIfIngredientsPresentInInventory():
    # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    blackTeaComposition = {"water": 200, "tea_syrup": 10}
    beverageUnderTest = Beverage("black tea",blackTeaComposition)
    # act
    machineUnderTest.make_beverage(beverageUnderTest)
    machineUnderTest.make_beverage(beverageUnderTest)

    # assert
    assert machineUnderTest.inventory["tea_syrup"] == basicTeaSyrupInventory - 2 * blackTeaComposition["tea_syrup"]
    assert machineUnderTest.inventory["water"] == basicWaterInventory - 2 * blackTeaComposition["water"]

@testDecorator
def canNotMakeABeverageIfIngredientsNotPresentInInventory():
    machineUnderTest = setupOneOutletMachineWithNoInventory()
    beverageUnderTest = setupBlackTea()
    assert machineUnderTest.make_beverage(beverageUnderTest) == False

@testDecorator
def canNotMakeABeverageIfIngredientsAreInsufficient():
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    beverageUnderTest = Beverage("Extreme Strong Tea", {"tea_syrup": 1000})
    assert machineUnderTest.make_beverage(beverageUnderTest) == False




def main():
    print("\nRunning Unit Tests ")
    refillCanAddNewIngredientsIfNotPresent()
    refillCanUpdateIngredientQuantityIfPresent()
    canMakeOneBeverageIfIngredientsPresentInInventory()
    canNotMakeABeverageIfIngredientsNotPresentInInventory()
    canNotMakeABeverageIfIngredientsAreInsufficient()

if __name__ == "__main__":
    main()
