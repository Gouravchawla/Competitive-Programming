#!/usr/bin/env python

'''
Source: http://opc.iarcs.org.in/index.php/problems/LEADGAME
'''

leader = []
lead = []
sum_si = 0
sum_ti = 0

# Number of rounds (test cases)
N = input()

while N:
    # Input score in one line
    line = raw_input()
    # Parse input into int
    si = int(line.split()[0])
    ti = int(line.split()[1])
    sum_si += si
    sum_ti += ti
    # If difference is less than 0, then 2 is the leader else 1
    if (sum_si - sum_ti) < 0:
        lead.append(-(sum_si - sum_ti))
        leader.append(2)
    else:
        lead.append(sum_si - sum_ti)
        leader.append(1)
    N -= 1


# Find max and it's index using Python's in-built functions
L = max(lead)
W = leader[lead.index(L)]

# Print results
print W, L
