#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is program


def main():
    # this function uses a try statement
    print("This program says number even or odd")

    # input
    integer1 = input("Enter the number: ")
    print("")

    # process & output
    try:
        number1 = int(integer1)
        if number1 == 0:
            print("This is zero")
        elif number1 % 2 == 0:
            print("This number is even")
        else:
            print("This number is odd")
    except Exception:
        print("Please enter number")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
