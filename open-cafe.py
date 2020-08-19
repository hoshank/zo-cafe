import json
import sys


from main.src.domain.beverageMaker import BeverageMaker
from main.src.domain.inventory import Inventory
from main.src.domain.machine import Machine
from main.src.domain.beverage import Beverage

from main.src.utils.jsonExtract import json_extract

def demoApp(jsonPath):

    json_data = json.loads(open(jsonPath, 'r').read())
    sample_machine = json_data['machine']
    outlet_count = json_extract(json_data['machine'],'count_n')[0]
    inventory = sample_machine['total_items_quantity']
    availableBeverages = sample_machine['beverages']

    zo_inventory = Inventory(inventory)

    beverage_list = list()

    for beverage in availableBeverages:
        beverage_list.append(Beverage(beverage, availableBeverages[beverage]))

    coffee_machine = Machine(outlet_count, zo_inventory, BeverageMaker())



    for beverage in beverage_list:
        coffee_machine.make_beverage(beverage)


def main(argv = 'resources/test/test.json'):
    print("inside main",argv)
    demoApp(argv)

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        main(sys.argv[1])
    else:
        main()