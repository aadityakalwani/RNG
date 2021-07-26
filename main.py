import random


def continue():

    # this is what will happen straight after printing "your number is xyz"

def first_rng():
    while True:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        print(f"Your random number is {random.randint(x, y)}")

        repeat_or_not = input("Press q to quit, or any other key to repeat")

        if repeat_or_not == "q":
            print("Thanks for using my RNG")
            break

        elif repeat_or_not != "q":
            same_numbers = input("Press y if you want the random number to be within the same range\n"
                                 "Press n if you want the random number to be within a different range\n"
                                 "Enter here:")

            if same_numbers == "y":
                print(f"Your random number is {random.randint(x, y)}")
                continue

            elif same_numbers == "n":
                new_rng()


def new_rng():
    while True:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        print(f"Your random number is {random.randint(x, y)}")

        repeat_or_not = input("Press q to quit, or any other key to repeat")

        if repeat_or_not == "q":
            print("Thanks for using my RNG")
            break

        elif repeat_or_not != "q":
            same_numbers = input("Press y if you want the random number to be within the same range\n"
                                 "Press n if you want the random number to be within a different range\n"
                                 "Enter here:")

            if same_numbers == "y":
                print(f"Your random number is {random.randint(x, y)}")
                continue

            elif same_numbers == "n":
                continue


first_rng()