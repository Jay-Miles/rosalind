#!usr/bin/env python

"""
Mendel's First Law
Topics: Heredity, Probability

Problem:
Probability is the mathematical study of randomly occurring phenomena. We
will model such a phenomenon with a random variable, which is simply a
variable that can take a number of different distinct outcomes depending on
the result of an underlying random process.

For example, say that we have a bag containing 3 red balls and 2 blue balls.
If we let X represent the random variable corresponding to the color of a
drawn ball, then the probability of each of the two outcomes is given by
Pr(X=red)=35 and Pr(X=blue)=25.

Random variables can be combined to yield new random variables. Returning to
the ball example, let Y model the color of a second ball drawn from the bag
(without replacing the first ball). The probability of Y being red depends
on whether the first ball was red or blue. To represent all outcomes of X
and Y, we therefore use a probability tree diagram. This branching diagram
represents all possible individual probabilities for X and Y, with outcomes
at the endpoints ("leaves") of the tree. The probability of any outcome is
given by the product of probabilities along the path from the beginning of
the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct,
the probability of an event can be written as the sum of the probabilities
of its constituent outcomes. For our colored ball example, let A be the
event "Y is blue." Pr(A) is equal to the sum of the probabilities of two
different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue), or
310+110=25 (see Figure 2 above).

Given:
Three positive integers k, m, and n, representing a population containing
k+m+n organisms: k individuals are homozygous dominant for a factor, m are
heterozygous, and n are homozygous recessive.

Return:
The probability that two randomly selected mating organisms will produce an
individual possessing a dominant allele (and thus displaying the dominant
phenotype). Assume that any two organisms can mate.

Sample Dataset:
2 2 2

Sample Output:
0.78333
"""


import argparse


def get_input(input_file):
    
    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()
    
    split_contents = file_contents.split(' ')

    genotype_counts = []

    for element in split_contents:
        stripped_element = element.strip()
        genotype_counts.append(int(stripped_element))

    return genotype_counts


def dominant_allele_prob(genotype_counts):
    """Given the 3 integers supplied in the argument, calculate the
    probability that the offspring of any two randomly selected individuals
    has at least one dominant allele.

    Args:
        genotype_counts [list]: 3-integer list

    Returns:
        probability [float]: calculated probability
    """

    # Get the number of individuals with each genotype
    hD = int(genotype_counts[0])
    het = int(genotype_counts[1])
    hR = int(genotype_counts[2])

    # Get the squared number of heterozygotes and dominant homozygotes
    hD_squared = hD ** 2
    het_squared = het ** 2

    # Get the total number of alleles
    total_alleles = 2 * (sum(genotype_counts))

    # Get number of alleles for the second choice, and the product
    alleles_minus_two = total_alleles - 2
    allele_denominator = total_alleles * alleles_minus_two

    # The equation to get the probability is:

    # 4 * (hD**2 – hD)/(TA**2 - 2TA) + 
    # 8 * hD * het/(TA**2 - 2TA) + 
    # 8 * hD * hR/(TA**2 - 2TA) + 
    # 4 * hR * Het/(TA**2 - 2TA) + 
    # 3 * (Het2 – Het)/(TA**2 - 2TA)

    # I am not going to write out the whole derivation here it's in a ppt

    probability = (
        ((4 * (hD_squared - hD)) / allele_denominator) + \
        ((8 * hD * het) / allele_denominator) + \
        ((8 * hD * hR) / allele_denominator) + \
        ((4 * hR * het) / allele_denominator) + \
        ((3 * (het_squared - het)) / allele_denominator)
        )

    return probability


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    genotype_counts = get_input(input_file)
    probability = dominant_allele_prob(genotype_counts)

    print(probability)


if __name__ == '__main__':
    main()
