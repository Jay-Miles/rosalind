#!usr/bin/env python

"""
Independent Alleles
Topics: Heredity, Probability

Problem:

Two events A and B are independent if Pr(A and B) is equal to
Pr(A)×Pr(B). In other words, the events do not influence each other, so
that we may simply calculate each of the individual probabilities
separately and then multiply.

More generally, random variables X and Y are independent if whenever A
and B are respective events for X and Y, A and B are independent (i.e.,
Pr(A and B)=Pr(A)×Pr(B)).

As an example of how helpful independence can be for calculating
probabilities, let X and Y represent the numbers showing on two
six-sided dice. Intuitively, the number of pips showing on one die
should not affect the number showing on the other die. If we want to
find the probability that X+Y is odd, then we don't need to draw a tree
diagram and consider all possibilities. We simply first note that for
X+Y to be odd, either X is even and Y is odd or X is odd and Y is even.

In terms of probability,
Pr(X+Y is odd)=Pr(X is even and Y is odd)+Pr(X is odd and Y is even).

Using independence, this becomes
[Pr(X is even)×Pr(Y is odd)]+[Pr(X is odd)×Pr(Y is even)],
or (12)2+(12)2=12. 

Given:
Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two
children in the 1st generation, each of whom has two children, and so
on. Each organism always mates with an organism having genotype Aa Bb.

Return:
The probability that at least N Aa Bb organisms will belong to the k-th
generation of Tom's family tree (don't count the Aa Bb mates at each
level). Assume that Mendel's second law holds for the factors.

Sample Dataset:
2 1

Sample Output:
0.684
"""


import argparse


def get_input(input_file):

    with open(input_file, 'r') as file_object:
        file_contents = file_object.read()
    
    contents_list = file_contents.split(' ')
    input_numbers = [int(x) for x in contents_list]

    return input_numbers


def find_probability(input_numbers):

    k = input_numbers[0]
    N = input_numbers[1]

    probability = 1

    for x in range(k, 0, -1):
        p_gen_x = N / (2 ** x)
        probability *= p_gen_x

    # gen 0: Aa Bb
    # gen 0 (and each descendant) produces 2 offspring with an Aa Bb individual
    # find: P = p(at least N Aa Bb offspring in generation k)

    # from Mendel's 2nd, p(Aa Bb) = p(Aa) * p(Bb)
    # For any (Aa Bb x Aa Bb) cross, p(offspring is Aa Bb) = 0.5 * 0.5 = 0.25
    # the probability that any one offspring is NOT Aa Bb is (1 - 0.25) = 0.75

    # an individual MUST be Aa Bb to be able to produce an Aa Bb offspring with
    # an Aa Bb partner

    # for generation a of k,
    # n(a) = total offspring in generation a = 2**k (max 128 when k=7)
    # m(a) =  Aa Bb offspring in generation a

    # 'AT LEAST N Aa Bb individuals in generation a', or m(a)>=N, means:
    # p(m(a)>=N)    = p(m(a)=N) + p(m(a)=(N+1)) + ... + p(m(a)=n(a))
    #               = sum of p(m(a)=i) for i in range(N, n(a), 1)

    # p(m(a)=i) depends on:
    #   the number of previous generations
    #   the number of Aa Bb individuals in gen a-1

    # to have i Aa Bb individuals in generation a, there must be at least i/2
    # (rounded up) Aa Bb individuals in generation a-1 (because each
    # individual has 2 offspring). This can be summarised as:

    #   if m(a)=i, m(a-1) must be >= i/2

    # however, the same is true for generation a-1: there must be at least
    # (i/2 * 1/2) Aa Bb individuals in generation a-2. This generalises to:

    #   if m(a)=i, m(a-b) must be >= i/(2**b) for b in range(1, k-1, 1)

    # This can be written as:

    # for generation in range(1, k+1):
    #   minimum_AaBb = N / (2 ** (k-g))

    # 




    # p(m>=N) = 0
    # for i in range(N, n, 1):
    #   p(m=i) = <needs solving>
    #   p(m>=N) += p(m=i)


    return probability


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    input_file = args.input_file
    input_numbers = get_input(input_file)
    probability = find_probability(input_numbers)

    print(probability)


if __name__ == '__main__':
    main()
