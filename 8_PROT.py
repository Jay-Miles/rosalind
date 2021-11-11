#!usr/bin/env python

"""
Translating RNA into Protein

Problem:
The 20 commonly occurring amino acids are abbreviated by using 20 letters
from the English alphabet (all letters except for B, J, O, U, X, and Z).
Protein strings are constructed from these 20 symbols. Henceforth, the term
genetic string will incorporate protein strings along with DNA strings and
RNA strings.

The RNA codon table dictates the details regarding the encoding of specific
codons into the amino acid alphabet.

Given:
An RNA string s corresponding to a strand of mRNA (of length at most 10 
kbp).

Return:
The protein string encoded by s.

Sample Dataset:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
"""


import argparse


def get_codon_aas():

    with open('codon_aa_pairs.txt', 'r') as file_object:
        pairs = file_object.readlines()

    codon_aa_pairs = []

    for line in pairs:
        stripped_line = line.strip()

        try:
            codon = stripped_line[:3]

            if stripped_line[-4:] == 'Stop':
                aa = stripped_line[-4:]
            
            else:
                aa = stripped_line[-1]

            codon_aa_pairs.append((codon, aa))
        
        except IndexError:
            continue

    return codon_aa_pairs


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()

    stripped_contents = file_contents.strip()
    rna_string = stripped_contents.replace('\n', '')

    return rna_string


def rna_2_protein(codon_aa_pairs, rna_string):

    protein_string = ''

    for i in range(0, len(rna_string), 3):  # Loop over every 3rd character
        start = i
        stop = i + 3
        codon = rna_string[start:stop]
        
        for tuple in codon_aa_pairs:
            if (tuple[0] == codon) and (tuple[1] != 'Stop'):
                protein_string += tuple[1]

    return protein_string


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file

    codon_aa_pairs = get_codon_aas()
    rna_string = get_input(input_file)
    protein_string = rna_2_protein(codon_aa_pairs, rna_string)

    print(protein_string)


if __name__ == '__main__':
    main()
