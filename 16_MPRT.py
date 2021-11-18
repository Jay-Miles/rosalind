#!usr/bin/env python

"""
Finding a Protein Motif
Topics: File Formats, Proteomics

Problem:
To allow for the presence of its varying forms, a protein motif is
represented by a shorthand as follows: [XY] means "either X or Y" and {X}
means "any amino acid except X." For example, the N-glycosylation motif is
written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein
by its access ID "uniprot_id" in the UniProt database, by inserting the ID
number into http://www.uniprot.org/uniprot/uniprot_id

Alternatively, you can obtain a protein sequence in FASTA format by
following http://www.uniprot.org/uniprot/uniprot_id.fasta

For example, the data for protein B5ZC00 can be found at
http://www.uniprot.org/uniprot/B5ZC00.

Given:
At most 15 UniProt Protein Database access IDs.

Return:
For each protein possessing the N-glycosylation motif, output its given
access ID followed by a list of locations in the protein string where the
motif can be found.

Sample Dataset:
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output:
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""


import argparse
import requests

from Bio import SeqIO
from io import StringIO
from ratelimit import limits


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.readlines()
    
    uniprot_ids = [line.strip() for line in file_contents]

    return uniprot_ids


@limits(calls=10, period=1)
def get_sequences(uniprot_ids):

    protein_sequences = {}

    for id in uniprot_ids:

        baseUrl = "http://www.uniprot.org/uniprot/"
        currentUrl = baseUrl + id + '.fasta'

        response = requests.post(currentUrl)

        raw_data = ''.join(response.text)
        string_object = StringIO(raw_data)
        iterator = SeqIO.parse(string_object, 'fasta')
        sequence_object = [record.seq for record in iterator]

        protein = str(sequence_object[0])
        protein_sequences[id] = protein

    return protein_sequences


def find_motifs(protein_sequences):

    motif_locations = {}

    for id, sequence in protein_sequences.items():

        locations = []

        for i in range(len(sequence)):

            try:
                if (sequence[i] == 'N') and \
                    (sequence[i+1] != 'P') and \
                    ((sequence[i+2] == 'S') or (sequence[i+2] == 'T')) and \
                    (sequence[i+3] != 'P'):

                    locations.append(str(i+1))

            except IndexError:
                continue
        
        if locations != []:
            motif_locations[id] = locations

    return motif_locations


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    uniprot_ids = get_input(input_file)
    protein_sequences = get_sequences(uniprot_ids)
    motif_locations = find_motifs(protein_sequences)

    for id, locations in motif_locations.items():
        print(id)
        print(' '.join(locations))


if __name__ == '__main__':
    main()
