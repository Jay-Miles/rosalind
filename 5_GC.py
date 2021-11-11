#!usr/bin/env python

"""
Computing GC Content
Topics: String Algorithms

Problem:
The GC-content of a DNA string is given by the percentage of symbols in the
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is
37.5%. Note that the reverse complement of any DNA string has the same
GC-content.

DNA strings must be labeled when they are consolidated into a database. A
commonly used method of string labeling is called FASTA format. In this
format, the string is introduced by a line that begins with '>', followed by
some labeling information. Subsequent lines contain the string itself; the
first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by
the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000
and 9999.

Given:
At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return:
The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in
all decimal answers unless otherwise stated; please see the note on absolute
error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    split_contents = file_contents.split('>')
    split_contents.remove('')

    ids_and_strings = []

    for element in split_contents:

        stripped_element = element.strip()
        no_newlines = stripped_element.replace('\n', '')

        dna_id = no_newlines[:13]
        dna_string = no_newlines[13:]

        ids_and_strings.append((dna_id, dna_string))
    
    return ids_and_strings


def get_highest_gc(ids_and_strings):
    """Of the DNA strings in ids_and_strings, identifies the DNA string with
    the highest GC content. Returns a 2-element list with the ID of this
    string and its GC content.

    Args:
        ids_and_strings [list]: list of tuples in form (dna_id, dna_string)

    Returns:
        highest_gc [list]: list in the form [DNA ID, GC content]
    """

    highest_gc = ['', 0]

    for dna_tuple in ids_and_strings:

        total_characters = len(dna_tuple[1])
        c_count = dna_tuple[1].count('C')
        g_count = dna_tuple[1].count('G')

        gc_content = 100 * ((c_count + g_count) / total_characters)

        if gc_content > highest_gc[1]:
            highest_gc = [dna_tuple[0], gc_content]
    
    return highest_gc


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    ids_and_strings = get_input(input_file)
    highest_gc = get_highest_gc(ids_and_strings)

    print(highest_gc[0])
    print(highest_gc[1])


if __name__ == '__main__':
    main()
