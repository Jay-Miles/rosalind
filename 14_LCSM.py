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
        records = [(record.id, record.seq) for record in iterator]
    
    return records


def get_longest_motif(records):

    # Find all substrings of all sequences
    print('Finding all substrings of first sequence')

    sequences = [record[1] for record in records]

    record_1 = sequences[0]
    record_1_length = len(record_1)

    record_1_substrings = [
        record_1[i:j] \
            for i in range(record_1_length) \
            for j in range(i + 1, record_1_length + 1)
        ]

    print('Checking if each substring is in all sequences')

    common_substrings = []
    
    for substring in record_1_substrings:
        in_all_sequences = all(
            substring in sequence for sequence in sequences
            )
        
        if in_all_sequences == True:
            common_substrings.append(substring)
    
    print('Finding longest shared substring')

    longest_motif = ''

    for substring in common_substrings:
        if len(substring) > len(longest_motif):
            longest_motif = substring

    return longest_motif


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    records = get_input(input_file)
    longest_motif = get_longest_motif(records)

    print(longest_motif)


if __name__ == '__main__':
    main()
