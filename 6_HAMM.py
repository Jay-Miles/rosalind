#!usr/bin/env python

"""
Counting Point Mutations
Topics: Alignment

Problem:
Given two strings s and t of equal length, the Hamming distance between s
and t, denoted dH(s,t), is the number of corresponding symbols that differ
in s and t. See Figure 2.

Given:
Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return:
The Hamming distance dH(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    stripped_contents = file_contents.strip()
    no_newlines = stripped_contents.replace('\n', '')

    total_length = len(no_newlines)
    half_length = int(0.5 * total_length)

    string_1 = no_newlines[:half_length]
    string_2 = no_newlines[half_length:]

    return string_1, string_2


def hamming_distance(string_1, string_2):

    difference_count = 0

    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            difference_count += 1
    
    return difference_count


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    string_1, string_2 = get_input(input_file)
    difference_count = hamming_distance(string_1, string_2)

    print(difference_count)


if __name__ == '__main__':
    main()
