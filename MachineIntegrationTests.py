from main.src.domain.machine import Machine
from main.src.domain.beverage import Beverage


import json

from main.src.domain.machine import Machine
from main.src.utils.jsonExtract import json_extract
from resources.test.decorators.testDecorator import testDecorator

'''
all tests written first to ensure Red, Green and Refactor

Used Decorator to display method name and result before it is executed
'''




def setupMachine(jsonPath):
    json_data = json.loads(open(jsonPath, 'r').read())
    sample_machine = json_data['machine']
    outlet_count = json_extract(sample_machine, 'count_n')[0]
    inventory = sample_machine['total_items_quantity']
    availableBeverages = sample_machine['beverages']
    return Machine(outlet_count, inventory),availableBeverages

@testDecorator
def shouldHaveInventoryAndBeverageCompositionLikeJSON():
    # arrange and act
    jsonPath = 'resources/test/testLowIngredients.json'


    json_data = json.loads(open(jsonPath, 'r').read())
    sample_machine = json_data['machine']
    expectedInventory = sample_machine['total_items_quantity']
    #act
    machineUnderTest, availableBeverages = setupMachine(jsonPath)
    expectedOutlets = 3
    #assert
    assert machineUnderTest.currentOrders == 0
    assert len(machineUnderTest.inventory) == len(expectedInventory) \
           and sorted(machineUnderTest.inventory) == sorted(expectedInventory)
    assert machineUnderTest.numberOfOutlets == expectedOutlets

@testDecorator
def shouldDisplayErrorForInsufficientIngredient():
    #arrange
    machineUnderTest,availableBeverages = setupMachine('resources/test/testLowIngredients.json')
    #act
    result =  machineUnderTest.make_beverage(Beverage("hot_tea",availableBeverages["hot_tea"]))
    #assert
    assert result == False

@testDecorator
def shouldDisplayErrorForUnavailableIngredient():
    #arrange
    machineUnderTest,availableBeverages = setupMachine('resources/test/testUnavailableIngredients.json')
    #act
    beverageUnderTest = Beverage("hot_tea",availableBeverages["hot_tea"])
    result =  machineUnderTest.make_beverage(beverageUnderTest)
    #assert
    assert result == False
    #assert beverageUnderTest.canPrepareBeverage.called

def main():
    print("\nRunning Integration Tests ")

    shouldHaveInventoryAndBeverageCompositionLikeJSON()

    shouldDisplayErrorForInsufficientIngredient()
    shouldDisplayErrorForUnavailableIngredient()

    #print("Hello World!")

if __name__ == "__main__":
    main()