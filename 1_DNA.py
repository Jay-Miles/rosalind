#!usr/bin/env python

"""
Counting DNA Nucleotides
Topics: String Algorithms

Problem:
A string is simply an ordered collection of symbols selected from some
alphabet and formed into a word; the length of a string is the number of
symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols
'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given:
A DNA string s of length at most 1000 nt.

Return:
Four integers (separated by spaces) counting the respective number of times
that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
"""


import argparse


def get_input(input_file):
    with open(input_file, 'r') as file_object:
        dna_string = file_object.read()

    print('DNA string to count nucleotides from:', dna_string)

    return dna_string


def count_nucleotides(dna_string):
    # Specify which characters to look for and initialise their counts
    nucleotides = ['A', 'C', 'G', 'T']
    counts = [0, 0, 0, 0]

    # Increment each count by looping over the string
    for character in dna_string:
        if character in nucleotides:
            position = nucleotides.index(character)
            counts[position] += 1

    # Format the counts for output
    output = '{A} {C} {G} {T}'.format(
        A = counts[0],
        C = counts[1],
        G = counts[2],
        T = counts[3],
        )

    return output


def main():
    # Initialise the argument parser
    parser = argparse.ArgumentParser(
        description = 'Supply a text file containing a DNA string to the script.'
        )

    # Add an argument to take the name of the input file
    parser.add_argument(
        'input_file',
        help = 'A text file containing a DNA string',
        )

    # Pass the supplied filename to the script
    args = parser.parse_args()
    input_file = args.input_file

    # Get the contents of the input file
    dna_string = get_input(input_file)

    # Count the number of each nucleotide
    output = count_nucleotides(dna_string)

    print(output)


if __name__ == '__main__':
    main()


# or as a one-liner...

# print(
# dna_string.count('A'),
# dna_string.count('C'),
# dna_string.count('G'),
# dna_string.count('T')
# )
