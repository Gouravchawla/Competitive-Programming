#!/usr/bin/env python

"""
Source: http://opc.iarcs.org.in/index.php/problems/VOTERS
"""


def main():
    n1, n2, n3 = map(int, raw_input().split())
    n1_list = {}
    n2_list = {}
    n3_list = {}
    voter_list = []

    # Take input
    n1_list = {int(raw_input()) for n in range(n1)}
    n2_list = {int(raw_input()) for n in range(n2)}
    n3_list = {int(raw_input()) for n in range(n3)}

    # Take intersection of possible list combinations and then union
    # Of those results. After that parse into a list and sort it.
    voter_list = sorted(list((n1_list & n2_list) | (n1_list & n3_list) | (n2_list & n3_list)))

    # Print out the result
    print len(voter_list)
    for idx in range(len(voter_list)):
        print voter_list[idx]


if __name__ == '__main__':
    main()
