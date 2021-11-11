#!usr/bin/env python

"""
Overlap Graphs
Topics: Graph Algorithms

Problem:
A graph whose nodes have all been labeled can be represented by an adjacency
list, in which each row of the list contains the two node labels
corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of
which has an orientation. That is, a directed edge is represented by an
arrow instead of a line segment; the starting and ending nodes of an edge
form its tail and head, respectively. The directed edge with tail v and head
w is represented by (v,w) (but not by (w,v)). A directed loop is a directed
edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for
the strings is a directed graph Ok in which each string is represented by a
node, and string s is connected to string t with a directed edge when there
is a length k suffix of s that matches a length k prefix of t, as long as
s≠t; we demand s≠t to prevent directed loops in the overlap graph (although
directed cycles may be present).

Given:
A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return:
The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""


import argparse
from Bio import SeqIO


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        iterator = SeqIO.parse(file_object, 'fasta')
        fasta_records = [(record.id, record.seq) for record in iterator]

    return fasta_records


def construct_graph(fasta_records):

    overlap_graph = []

    for record_1 in fasta_records:
        for record_2 in fasta_records:
            if record_1 != record_2:
                if record_1[1][-3:] == record_2[1][:3]:
                    sentence = '{a} {b}'.format(a=record_1[0], b=record_2[0])
                    overlap_graph.append(sentence)

    return overlap_graph


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    fasta_records = get_input(input_file)
    overlap_graph = construct_graph(fasta_records)

    for directed_node in overlap_graph:
        print(directed_node)


if __name__ == '__main__':
    main()
