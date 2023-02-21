#!/usr/env/python3
if __name__ == "__main__":

    def main():

        mylist= [1,2,3,4,5, "Python"]

        name= input("What is your name?\n>")

        # This is what you should see when print runs-
        # Hi <name>! Welcome to Day 2 of Python Training!
        print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")

    main()
