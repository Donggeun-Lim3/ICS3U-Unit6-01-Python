#!/usr/bin/env python3

# Created by: Donggeun Lim
# Created on: Jan 2019
# This program calculates average of 10 random numbers

import random


def main():
    # this function displays 10 random number with the array

    my_numbers = []

    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        my_numbers.append(a_number)
        print("The random number is: {0} ".format(my_numbers[loop_counter]),
              end="" + "\n")
    average = (my_numbers[0] + my_numbers[1] + my_numbers[2] + my_numbers[3]
               + my_numbers[4] + my_numbers[5] + my_numbers[6] + my_numbers[7]
               + my_numbers[8] + my_numbers[9]) / 10
    print("")
    print("The average is {0}".format(average))


if __name__ == "__main__":
    main()
