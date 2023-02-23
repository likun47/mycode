#!/usr/bin/env python3

import time

# the greeting message
def welcome_message():
    print("Welcome to the Pizza Order system!")
    time.sleep(1)
    print("Answer a few questions and we'll recommend the perfect pizza for you!")
    time.sleep(1)

#return crust type after custer select a curst.
def get_crust_type():
    while True:
        try:
            crust = input("What type of crust do you prefer? (thin, thick, or stuffed) ")
            if crust.lower() in ['thin', 'thick', 'stuffed']:
                return crust.lower()
            else:
                print("Sorry, that's not a valid option. Please try again.")
        except:
            print("Sorry, something went wrong. Please try again.")


# return a topping list after customer select one and one more options
def get_toppings():
    toppings = []
    while True:
        try:
            topping = input("What toppings do you like on your pizza? (type 'done' when finished) ")
            if topping.lower() == 'done': #in case you finish the selection but the function still running. 
                if len(toppings) == 0: 
                    print("Sorry, you need to choose at least one topping. Please try again.")
                else:
                    return toppings
            elif topping.lower() in ['pepperoni', 'sausage', 'mushrooms', 'onions', 'peppers', 'olives']:
                toppings.append(topping.lower())
                print("Added " + topping.lower() + " to your pizza!")
            else:
                print("Sorry, we don't have " + topping.lower() + " as an option. Please try again.")
        except:
            print("Sorry, something went wrong. Please try again.")

#size selection
def get_size():
    while True:
        try:
            size = input("What size pizza do you want? (small, medium, or large) ")
            if size.lower() in ['small', 'medium', 'large']:
                return size.lower()
            else:
                print("Sorry, that's not a valid option. Please try again.")
        except:
            print("Sorry, something went wrong. Please try again.")


#print out your selections.
def recommend_pizza(crust, toppings, size):
    print("Based on your preferences, we recommend a " + size + " " + crust + " crust pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    print("Enjoy your pizza!")

#main function
def main():
    welcome_message()
    crust_type = get_crust_type()
    pizza_toppings = get_toppings()
    pizza_size = get_size()
    recommend_pizza(crust_type, pizza_toppings, pizza_size)

if __name__ == '__main__':
    main()

