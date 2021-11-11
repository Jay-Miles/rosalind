#!usr/bin/env python

"""
Complementing a Strand of DNA
Topics: String Algorithms

Problem:
In DNA strings, symbols 'A' and 'T' are complements of each other, as are
'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by
reversing the symbols of s, then taking the complement of each symbol (e.g.,
the reverse complement of "GTCA" is "TGAC").

Given:
A DNA string s of length at most 1000 bp.

Return:
The reverse complement sc of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""


import argparse


def get_input(input_file):
    # Get the contents of the specified text file
    with open(input_file, 'r') as file_object:
        dna_string = file_object.read()

    print('DNA string to reverse complement:', dna_string)

    return dna_string


def reverse_complement(dna_string):
    # Reverse the DNA string
    reversed_string = dna_string[::-1]

    # Define the complement of each nucleotide
    nucleotides = ['A', 'C', 'G', 'T']
    complements = ['T', 'G', 'C', 'A']

    # Initialise a string to hold the output string
    rev_complement = ''

    # Loop over the DNA string and add rev-comp nucleotides to the new string
    for character in reversed_string:
        if character in nucleotides:
            position = nucleotides.index(character)
            rev_complement += complements[position]
    
    return rev_complement


def main():
    # Construct an argument parser to pass input file to script
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file

    # Get the DNA string from the input file
    dna_string = get_input(input_file)

    # Get the reverse complement
    rev_complement = reverse_complement(dna_string)

    print('Reverse complemented string:', rev_complement)


if __name__ == '__main__':
    main()
