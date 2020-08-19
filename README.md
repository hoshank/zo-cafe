# zo-cafe
Design a OO Coffee Machine

# 1. Description
The app has been built in vanilla Python without any framework like Django. The primary reason to use Python was to produce the working system with minimal code in lowest possible time.The app has been designed keeping SOLID principles in mind along with appropriate design patterns to ensure extensibility. Decorators have been used where deemed appropriate. No Design is perfect in first go. There could be scope for a better design.

# 2. Setup and Run
The app has been dockerised for easy run. To build a docker image run the following commands in the root directory of the project


docker build -t zo-cafe:latest .

docker run -it --rm --name my-zo-cafe zo-cafe