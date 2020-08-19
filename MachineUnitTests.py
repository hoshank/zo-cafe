from main.src.domain.beverageMaker import BeverageMaker
from main.src.domain.inventory import Inventory
from main.src.domain.machine import Machine
from main.src.domain.beverage import Beverage

from resources.test.decorators.testDecorator import testDecorator

basicMilkQuantity = 1000
basicWaterQuantity = 1000
basicCocoaQuantity = 200
basicTeaSyrupQuantity = 100

emptyInventory = Inventory({})

basicInventory = Inventory({"milk": basicMilkQuantity,
                            "water": basicWaterQuantity,
                            "cocoa": basicCocoaQuantity,
                            "tea_syrup": basicTeaSyrupQuantity})

sampleBeverages = [
    Beverage("Kashmiri Kahwa", {
        "kasmiri_tea_leaves": 10,
        "hot_water": 200
    }),
    Beverage("black tea", {
        "water": 200,
        "tea_syrup": 10
    })
]



def setupOneOutletMachineWithNoInventory():
    simpleBeverageMaker = BeverageMaker()
    return Machine(1, emptyInventory,simpleBeverageMaker)


def setupOneOutletMachineWithBasicInventory():
    simpleBeverageMaker = BeverageMaker()
    return Machine(1, basicInventory,
                   simpleBeverageMaker)


def setupBlackTea():
    return Beverage("black tea", {"water": 200, "tea_syrup": 10})


@testDecorator
def refillCanAddNewIngredientsIfNotPresent():
    # arrange
    machineUnderTest = setupOneOutletMachineWithNoInventory()
    # act
    machineUnderTest.inventory.refill("cocoa", 100)
    # assert
    assert len(machineUnderTest.inventory.inventory) == 1
    assert machineUnderTest.inventory.inventory["cocoa"] == 100


@testDecorator
def refillCanUpdateIngredientQuantityIfPresent():
    # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    # act
    itemQuantityToUpdate = 100
    itemUnderTest = "cocoa"
    machineUnderTest.inventory.refill(itemUnderTest, itemQuantityToUpdate)
    # assert
    assert machineUnderTest.inventory.inventory["cocoa"] == basicCocoaQuantity + itemQuantityToUpdate
    assert machineUnderTest.inventory.inventory["milk"] == basicMilkQuantity


@testDecorator


def canNotMakeABeverageIfIngredientsNotPresentInInventory():

    machineUnderTest = setupOneOutletMachineWithNoInventory()
    beverageUnderTest = Beverage("black tea", {"water": 200, "tea_syrup": 10})
    result= machineUnderTest.make_beverage(beverageUnderTest)
   # assert result == False

@testDecorator
def simpleMachineCanMakeOneBeverageIfIngredientsPresentInInventory():
    # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    beverageUnderTest = Beverage("black tea", {"water": 200, "tea_syrup": 10})
    print("Intial tea syrup quantity" , machineUnderTest.inventory.inventory["tea_syrup"])

    # act
    machineUnderTest.make_beverage(beverageUnderTest)
    # assert
    print("Updated tea syrup quantity" , machineUnderTest.inventory.inventory["tea_syrup"])
    assert machineUnderTest.inventory.inventory["tea_syrup"] == basicTeaSyrupQuantity - beverageUnderTest.composition["tea_syrup"]
    assert machineUnderTest.inventory.inventory["water"] == basicWaterQuantity - beverageUnderTest.composition["water"]


@testDecorator
def simpleMachineCanMakeTwoMoreBeverageIfIngredientsPresentInInventory():
    # arrange
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    blackTeaComposition = {"water": 200, "tea_syrup": 10}
    beverageUnderTest = Beverage("black tea", blackTeaComposition)
    print("Intial tea syrup quantity" , machineUnderTest.inventory.inventory["tea_syrup"])

    # act
    machineUnderTest.make_beverage(beverageUnderTest)
    print("Updated tea syrup quantity" , machineUnderTest.inventory.inventory["tea_syrup"])

    machineUnderTest.make_beverage(beverageUnderTest)
    print("Updated tea syrup quantity" , machineUnderTest.inventory.inventory["tea_syrup"])


    # assert
    assert machineUnderTest.inventory.inventory["tea_syrup"] == basicTeaSyrupQuantity - 3 * blackTeaComposition["tea_syrup"]
    assert machineUnderTest.inventory.inventory["water"] == basicWaterQuantity - 3 * blackTeaComposition["water"]





@testDecorator
def canNotMakeABeverageIfIngredientsAreInsufficient():
    machineUnderTest = setupOneOutletMachineWithBasicInventory()
    beverageUnderTest = Beverage("Extreme Strong Tea", {"tea_syrup": 1000})
    machineUnderTest.make_beverage(beverageUnderTest)


def main():
    print("\nRunning Unit Tests ")

    refillCanAddNewIngredientsIfNotPresent()
    refillCanUpdateIngredientQuantityIfPresent()


    simpleMachineCanMakeOneBeverageIfIngredientsPresentInInventory()

    simpleMachineCanMakeTwoMoreBeverageIfIngredientsPresentInInventory()


    canNotMakeABeverageIfIngredientsNotPresentInInventory()


    canNotMakeABeverageIfIngredientsAreInsufficient()




if __name__ == "__main__":
    main()
