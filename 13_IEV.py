#!usr/bin/env python

"""
Calculating Expected Offspring
Topics: Heredity, Probability

Problem:
For a random variable X taking integer values between 1 and n, the expected
value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of
taking the long-term average of a random variable over a large number of
trials.

As a motivating example, let X be the number on a six-sided die. Over a
large number of rolls, we should expect to obtain an average of 3.5 on the
die (even though it's not possible to roll a 3.5). The formula for expected
value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally
spaced outcomes has the same probability is called a uniform random variable
(in the die example, this "equal spacing" is equal to 1). We can generalize
our die example to find that if X is a uniform random variable with minimum
possible value a and maximum possible value b, then E(X)=a+b2. You may also
wish to verify that for the dice example, if Y is the random variable
associated with the outcome of a second die roll, then E(X+Y)=7.

Given:
Six nonnegative integers, each of which does not exceed 20,000. The integers
correspond to the number of couples in a population possessing each genotype
pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return:
The expected number of offspring displaying the dominant phenotype in the
next generation, under the assumption that every couple has exactly two
offspring.

Sample Dataset:
1 0 0 1 0 1

Sample Output:
3.5
"""


import argparse
from types import GeneratorType


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()
    
    split_contents = file_contents.split(' ')
    genotype_counts = [int(element) for element in split_contents]

    return genotype_counts


def p_dominant_phenotype(genotype_counts):

    dominant_probabilities = [1, 1, 1, 0.75, 0.5, 0]

    probability = 0

    for i in range(len(genotype_counts)):
        probability += (2 * genotype_counts[i] * dominant_probabilities[i])

    return probability


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    genotype_counts = get_input(input_file)
    probability = p_dominant_phenotype(genotype_counts)

    print(probability)


if __name__ == '__main__':
    main()
