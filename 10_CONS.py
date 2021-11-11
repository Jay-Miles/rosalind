#!usr/bin/env python

"""
Consensus and Profile
Topics: String Algorithms

Problem:
A matrix is a rectangular table of values divided into rows and columns. An
m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to
indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n.
Their profile matrix is a 4×n matrix P in which P1,j represents the number
of times that 'A' occurs in the jth position of one of the strings, P2,j
represents the number of times that C occurs in the jth position, and so on
(see below).

A consensus string c is a string of length n formed from our collection by
taking the most common symbol at each position; the jth symbol of c
therefore corresponds to the symbol having the maximum value in the j-th
column of the profile matrix. Of course, there may be more than one most
common symbol, leading to multiple possible consensus strings.

            A T C C A G C T
            G G G C A A C T
            A T G G A T C T
DNA Strings	A A G C A A C C
            T T G G A A C T
            A T G C C A T T
            A T G G C A C T

            A   5 1 0 0 5 5 0 0
Profile	    C   0 0 1 4 2 0 6 1
            G   1 1 6 3 0 1 0 0
            T   1 5 0 0 0 1 1 6

Consensus	    A T G C A A C T

Given:
A collection of at most 10 DNA strings of equal length (at most 1 kbp) in
FASTA format.

Return:
A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

Sample Dataset:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""


import argparse
from Bio import SeqIO


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        iterator = SeqIO.parse(file_object, 'fasta')
        list_of_sequences = [record.seq for record in iterator]

    return list_of_sequences


def get_profile_matrix(list_of_sequences):

    sequence_length = len(list_of_sequences[0])
    nucleotides = ['A', 'C', 'G', 'T']

    # matrix starts as {'A' : [0 0 0 ...], 'C' : [0 0 0 ...], ...}
    profile_matrix = {}
    for nucleotide in nucleotides:
        profile_matrix[nucleotide] = [0] * sequence_length
    
    # count & record numbers of each nucleotide at each position
    for sequence in list_of_sequences:
        for i in range(sequence_length):
            for nucleotide in nucleotides:
                if sequence[i] == nucleotide:
                    profile_matrix[nucleotide][i] += 1

    return sequence_length, nucleotides, profile_matrix


def get_consensus(sequence_length, nucleotides, profile_matrix):

    consensus_sequence = ''

    for i in range(sequence_length):
        highest_count = 0
        consensus_nucleotide = ''

        for nucleotide in nucleotides:
            if profile_matrix[nucleotide][i] > highest_count:
                highest_count = profile_matrix[nucleotide][i]
                consensus_nucleotide = nucleotide
        
        consensus_sequence += consensus_nucleotide

    # format profile matrix for correct output
    for key, value in profile_matrix.items():
        new_value = ''

        for i in range(sequence_length):
            new_value += str(value[i])
            new_value += ' '
        
        profile_matrix[key] = new_value

    return consensus_sequence


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file

    list_of_sequences = get_input(input_file)

    sequence_length, nucleotides, profile_matrix = get_profile_matrix(
        list_of_sequences
        )

    consensus_sequence = get_consensus(
        sequence_length,
        nucleotides,
        profile_matrix,
        )

    print(consensus_sequence)
    
    for nucleotide in nucleotides:
        print('{a}: {b}'.format(a=nucleotide, b=profile_matrix[nucleotide]))


if __name__ == '__main__':
    main()
