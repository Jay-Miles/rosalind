#!usr/bin/env python

"""
Mortal Fibonacci Rabbits
Topics: Combinatorics, Dynamic Programming

Problem:
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed
that each pair of rabbits reaches maturity in one month and produces a
single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed
number of months. See Figure 4 for a depiction of a rabbit tree in which
rabbits live for three months (meaning that they reproduce only twice before
dying).

Given:
Positive integers n≤100 and m≤20.

Return:
The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.

Sample Dataset:
6 3

Sample Output:
4
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()
    
    contents_list = file_contents.split()
    input_numbers = [int(number) for number in contents_list]

    return input_numbers


def count_final_rabbits(input_numbers):

    n = input_numbers[0]
    m = input_numbers[1]

    # Make a list of length m where the 1st element is 1 and the rest are 0
    # This represents the number of rabbit pairs at each month of age
    # i.e. when starting, there is 1 pair at age 0 and no others
    starting_rabbits = [1]
    starting_rabbits.append(0 * m)

    # This is what is present in the 1st month
    all_months = [starting_rabbits,]

    # For each month,
    for month in range(n-1):

        last_months_rabbits = all_months[month]
        current_month = []

        # 1st element is the sum of the previous month's [1:] elements
        current_month.append(sum(last_months_rabbits[1:]))

        # For each age of rabbit pairs after 0,
        for age in range(1, m):
            # Each subsequent element is [age-1] from previous month
            try:
                current_month.append(all_months[month][age-1])
            
            except IndexError:
                continue
        
        all_months.append(current_month)

    final_rabbits = sum(all_months[-1])

    return final_rabbits


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    input_numbers = get_input(input_file)
    final_rabbits = count_final_rabbits(input_numbers)

    print(final_rabbits)


if __name__ == '__main__':
    main()
