#!usr/bin/env python

"""
Finding a Shared Motif
Topics: String Algorithms

Problem:
A common substring of a collection of strings is a substring of every member
of the collection. We say that a common substring is a longest common
substring if there does not exist a longer common substring. For example,
"CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as
long as possible; in this case, "CGTA" is a longest common substring of
"ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a
simple example, "AA" and "CC" are both longest common substrings of "AACC"
and "CCAA".

Given:
A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA
format.

Return:
A longest common substring of the collection. (If multiple solutions exist,
you may return any single solution.)

Sample Dataset:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output:
AC
"""


import argparse
from Bio import SeqIO


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        iterator = SeqIO.parse(input_file, 'fasta')
        sequences = [(record.id, record.seq) for record in iterator]
    
    return sequences


def get_longest_motif(sequences):

    # Find all substrings of all sequences
    print('Finding all sequence substrings')

    substrings_dict = {}

    for record in sequences:

        sequence = record[1]
        seq_length = len(sequence)

        substrings = [
            sequence[i:j] \
            for i in range(seq_length) \
            for j in range(i + 1, seq_length + 1)
            ]

        substrings_dict[record[0]] = substrings

    # Identify longest common motif
    print('Finding longest common motif')

    longest_motif = ''
    motif_length = 0

    for motif in common_motifs:
        if len(motif) > motif_length:
            longest_motif = motif
            motif_length = len(motif)

    return longest_motif


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    sequences = get_input(input_file)
    longest_motif = get_longest_motif(sequences)

    print(longest_motif)


if __name__ == '__main__':
    main()
