#!usr/bin/env python

"""
Rabbits and Recurrence Relations
Topics: Combinatorics, Dynamic Programming

Problem:
A sequence is an ordered collection of objects (usually numbers), which are
allowed to repeat. Sequences can be finite or infinite. Two examples are the
finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers
(1,3,5,7,9,…). We use the notation an to represent the n-th term of a
sequence.

A recurrence relation is a way of defining the terms of a sequence with
respect to the values of previous terms. In the case of Fibonacci's rabbits
from the introduction, any given month will contain the rabbits that were
alive the previous month, plus any new offspring. A key observation is that
the number of offspring in any month is equal to the number of rabbits that
were alive two months prior. As a result, if Fn represents the number of
rabbit pairs alive after the n-th month, then we obtain the Fibonacci
sequence having terms Fn that are defined by the recurrence relation
Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence
bears Fibonacci's name, it was known to Indian mathematicians over two
millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation,
we can simply use the recurrence relation to generate terms for
progressively larger values of n. This problem introduces us to the
computational technique of dynamic programming, which successively builds up
solutions by using the answers to smaller cases.

Given:
    Two positive integers 'n' and 'k' in the form: n k
    Where...
        n = number of months that have passed (≤40)
        k = number of offsprint produced per pair per month (≤5)

Return:
    The total number of rabbit pairs present after n months.
    Assume the number of rabbit pairs at (n=1) is 1.

Sample Dataset:
    5 3

Sample Output:
    19

"""


import argparse


def get_input(input_file):
    """Extracts the input values n and k from the input text file.

    Args:
        input_file [string]: name of text file containing input

    Returns:
        n [int]: number of months that have passed (≤40)
        k [int]: k = number of offsprint produced per pair per month (≤5)
    """

    # Get the contents of the file
    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    # Split file contents on spaces, initialise a new list to hold integers
    contents_list = file_contents.split(' ')
    number_list = []

    # If elements of the split file are integers, add them to the new list
    for element in contents_list:
        if int(element):
            number_list.append(int(element))

    # If there are only 2 numbers in this list, these are n and k
    if len(number_list) == 2:

        n = number_list[0]
        k = number_list[1]

        return n, k

    # If there are not exactly 2 integers in the list, error out
    else:
        print('Error: Wrong number of inputs. List of inputs: ')
        print(number_list)


def get_rabbit_pairs(n, k):
    """Calculate the current number of rabbit pairs based on n and k.

    Args:
        n [int]: number of months that have passed (≤40)
        k [int]: k = number of offsprint produced per pair per month (≤5)
    
    Returns:
        current_pairs [int]: the current number of rabbit pairs
    """

    # Define the number of starting pairs
    starting_pairs = 1

    # Create a list to hold the total number of rabbit pairs in each month
    # The number of starting pairs is month 0
    progression = [(0, starting_pairs),]

    # For each month,
    for month in range(n-1):

        # Work out how many adult and young rabbits there are
        total_young = k * progression[month][0]
        total_adults = progression[month][0] + progression[month][1]

        # Get the new total by adding the new pairs to the old
        month_total = (total_adults, total_young)

        # This new total becomes the next value in the list
        progression.append(month_total)

    return progression


def main():
    # Construct a parser to pass a text file name to the script
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file

    # Extract the input numbers from the text file contents
    try:
        n, k = get_input(input_file)

        # Make a list of the rabbit pairs in consecutive months
        progression = get_rabbit_pairs(n, k)

        # The result is the total of the last value in the list
        final_numbers = progression[-1]
        total_pairs = sum(final_numbers)

        print('Final number of rabbit pairs:', str(total_pairs))

    except Exception:
        print('Error in getting input numbers.')


if __name__ == '__main__':
    main()
