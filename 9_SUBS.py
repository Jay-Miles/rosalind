#!usr/bin/env python

"""
Finding a Motif in DNA

Problem:
Given two strings s and t, t is a substring of s if t is contained as a
contiguous collection of symbols in s (as a result, t must be no longer than
s).

The position of a symbol in a string is the total number of symbols found to
its left, including itself (e.g., the positions of all occurrences of 'U' in
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position
i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the
starting and ending positions of the substring in s; for example, if
s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t
will have multiple locations in s if it occurs more than once as a substring
of s (see the Sample below).

Given:
Two DNA strings s and t (each of length at most 1 kbp).

Return:
All locations of t as a substring of s.

Sample Dataset:
GATATATGCATATACTT
ATAT

Sample Output:
2 4 10
"""

# Note: ROSALIND requires positions to be (i + 1) because it's wrong


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()
    
    stripped_contents = file_contents.strip()
    string1, string2 = stripped_contents.split('\n')

    return string1, string2


def find_substrings(string1, string2):

    positions = []

    str1_length = len(string1)
    str2_length = len(string2)

    for i in range(str1_length):
        if string1[i : (i + str2_length)] == string2:
            positions.append(str(i))
    
    output = ' '.join(positions)

    return output


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file

    string1, string2 = get_input(input_file)
    output = find_substrings(string1, string2)

    print(output)


if __name__ == '__main__':
    main()
