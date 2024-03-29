# CalculatorLibrary
### Scientific Calculator using python with unit tests and continuous integration with CircleCI. This application performs the below functionalities:

## Arithmetic operations
1.  Addition
2.  Subtraction
3.  Multiplication
4.  Division
5.  Square Root
6.  Cubic Root
7.  Factorial
8.  Power
9.  Modulus
10. Length of a Vector


## Trigonometric functionalities
11. Cosine of an angle in radians/degrees
12. Sine of an angle in radians/degrees
13. Tan of an angle in radians/degrees
14. Inverse cosine
15. Inverse sine
16. Inverse tan
17. Logarathmic for any given base, default base is e.

## Memory register
18. Store a value in memory
19. Display the memory register
20. Remove the value stored in memory register.
21. Use stored value for calculations (add/sub)

## Generate Reports
22. Generate reports for given day.
23. Generate reports within the given dates.


## Prerequisistes for linting and testing
pytest
pytest-cov
flake8  


## Download
git clone https://github.com/naveen1994rai/CalculatorLibrary.git

cd CalculatorLibrary


## Usage

### To use command line interactive application
python calculator.py

### To use via APIs with curl
1. Open a new terminal / command prompt

python calculator_api.py


2. Open another terminal / command prompt

Submit curl http requests


## Automated tests
pytest -v --cov


## Linting check (Optional)
flake8 --statistics

Note: Linting hasn't been performed for this project.

## API Documentation:
Check the project wiki on github for the API documentation.

## Note (For Python3 and Windows)
* If using python3, replace raw_input() func. with input() in calculator.py
* If using Windows, escape additional single or double quotes with a backslash when using curl.

curl -X POST -H "Content-Type: application/json"  -d "{ \"start\":\"2019-08-01\",\"end\":\"2019-08-03\" }" http://127.0.0.1:5000/query_by_range_Date
