#!/usr/bin/env python3

# Created by: Nathan Araujo
# Created on: December 7, 2022
# This program round the persons number depending on
# how many decimal places the user enters


# This function round the users number to the amount of decimal places they want
def round_num(num, num_decimals):
    # Multiples the users number by 10 to the power of num_decimals
    num[0] *= 10**num_decimals

    # Adds 0.5 to the users number
    num[0] += 0.5

    # Casts users number to an int
    num[0] = int(num[0])

    # Divides the user num by 10 to the power of num_decimals
    num[0] /= 10**num_decimals


def main():
    # Uses a try catch to catch any errors
    try:
        # Asks user for the number they want to round
        user_num = float(input("Enter a decimal number: "))

        # Asks user how many decimal places they want to round to
        user_decimals = int(
            input("Enter the number of decimal places you want to round to: ")
        )
    except Exception:
        print("You entered invalid number(s)!")
    else:
        # Declares user_num_list to an empty list
        user_num_list = []

        # Adds user's number to the list
        user_num_list.append(user_num)

        # Calls round_num(user_num_list, user_decimals)
        round_num(user_num_list, user_decimals)

        # Displays to user their rounded number
        print(f"{user_num} rounded to {user_decimals} places: {user_num_list[0]}")


if __name__ == "__main__":
    main()
