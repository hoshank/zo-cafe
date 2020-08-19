# zo-cafe
Design a OO Coffee Machine

# 1. Description
The app has been built in vanilla Python without any framework like Django. The primary reason to use Python was to produce the working system with minimal code in lowest possible time.The app has been designed keeping SOLID principles in mind along with appropriate design patterns to ensure extensibility. Decorators have been used where deemed appropriate. No Design is perfect in first go. There could be scope for a better design.

# 2. Setup and Run
This is a Python 3 app. This should run on Python 3.5+

To run the zo-cafe use command

python open-cafe.py [path to test JSON]

You can additionally provide a path to the JSON file

example 

python open-cafe.py resources/test/test.json

# 3. Unit and Integration Tests

Not all Unit and Integration Tests have been implemented
Unit Testing does not use unittest python package

Unit Test for Machine can be run by

python MachineUnitTests.py

Integration Test for Machine can be run by

python MachineIntegrationTests.py