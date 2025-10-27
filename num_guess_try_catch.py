#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/27/2025
# number guesser using try catch
import random


def main():
    # Ask the User to pick a number from 0 to 9:
    try:
        user_number = int(input("Pick a number between 0 and 9: "))

        # Generate a random number between 0 and 9
        random_number = random.randint(0, 9)

        # If User is correct
        if user_number == random_number:
            print("You guessed correctly!")

        # If User is wrong
        else:
            print("Incorrect the number was", random_number)
        
        # If user inputs a string
    except ValueError:
        print("No Idea")


if __name__ == "__main__":
    main()
