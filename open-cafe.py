import json

from main.src.domain.machine import Machine
from main.src.domain.beverage import Beverage
from main.src.utils.jsonExtract import json_extract

def test():

    json_data = json.loads(open('resources/test/test.json', 'r').read())
    sample_machine = json_data['machine']
    outlet_count = json_extract(json_data['machine'],'count_n')[0]
    inventory = sample_machine['total_items_quantity']
    availableBeverages = sample_machine['beverages']

    beverage_list = list()

    for beverage in availableBeverages:
        beverage_list.append(Beverage(beverage, availableBeverages[beverage]))

    coffee_machine = Machine(outlet_count, inventory)

    for beverage in beverage_list:
        coffee_machine.make_beverage(beverage)




def main():
    test()
    #print("Hello World!")

if __name__ == "__main__":
    main()