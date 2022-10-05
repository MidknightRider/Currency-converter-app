# **CURRENCY CONVERTER**

## Video link:
https://youtu.be/73ufiQTq71o
## Description:
As the title suggests, the program converts currency from one denomination to another.
Written in python, the program contains 4 functions and a main.
The program requires Regular Expressions (re) and the requests library. It also uses the sys module which comes pre-installed in Python.

The show_currencies() function takes one arguement which is the API URL. It returns the rates dictionary from the JSON.

The convert() funtion takes three arguements, which are the denomination we want to convert from, the denomination we want to convert to and amount of currency we want to convert. Since our base is USD, if the from_currency is not USD, we need to first convert it to USD. Then it is converted to the required denomination and it precision is limited to 4 decimal digits.

The output() function takes three arguements, again, the denomination we want to convert from, the denomination we want to convert to and amount of currency we want to convert. It applies the convert function on the arguements received returns the converted amount in the form of a statement.In case the user enters an invalid denomination, the program exits using sys.exit.

The numbers_only() function takes a string as an arguement and makes sure it is a valid amount. In case there are any commas present, they are removed using the replace() method. If the user inputs an invalid input, the program exits using sys.exit.

The main() function prints the title, just for aesthetics. If the user inputs 'rates' in the command line, show_currencies is called to display all the possible denominations which can be converted. The main() then takes inputs for the currency user wants to convert from, the currency user wants to convert to and the amount to be converted. The amount is converted to a floating value for use in functions used. The main() then prints the output returned by the output funtions which takes the three inputs received as arguements.

## Challenges and Experience
The project helped me get a better understanding of how to work with APIs. One of the problems I got stuck on was writting unit tests for functions which return varying values, like convert() and output().

## How to run the project:
The program can be executed simply by running the project.py file.

```
~/python project.py
```

## Tests:
test_projects.py contains various tests written to check the funtions and the program overall.
```
~/pytest test_project.py
```

### Check requirements.txt for all the libraries/modules used for functioning of program.