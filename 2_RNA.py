#!usr/bin/env python

"""
Transcribing DNA into RNA
Topics: String Algorithms

Problem:
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G',
and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA
string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given:
A DNA string t having length at most 1000 nt.

Return:
The transcribed RNA string of t.

Sample Dataset:
GATGGAACTTGACTACGTAAATT

Sample Output:
GAUGGAACUUGACUACGUAAAUU
"""


import argparse


def get_input(input_file):
    # Read in file contents as a DNA string
    with open(input_file, 'r') as file_object:
        dna_string = file_object.read()

    print('DNA string to convert to RNA:', dna_string)

    return dna_string


def dna_to_rna(dna_string):
    # Initialise the RNA string, and a list of nucleotides which don't change
    rna_string = ''
    static_nucleotides = ['A', 'C', 'G']

    # Sequentially add characters to the new string
    for character in dna_string:
        if character in static_nucleotides:
            rna_string += character
        
        elif character == 'T':
            rna_string += 'U'
    
    return rna_string


def main():
    # Construct an argument parser to pass a filename to the script
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    # Get the input file to look at
    input_file = args.input_file

    # Get the contents of the input file
    dna_string = get_input(input_file)

    # Convert the DNA string to RNA
    rna_string = dna_to_rna(dna_string)

    print('Converted string:', rna_string)


if __name__ == '__main__':
    main()
