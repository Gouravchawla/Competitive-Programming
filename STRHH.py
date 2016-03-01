# your code goes here
from __future__ import print_function


t = input()

while t:
    sequence_2k = raw_input()
    for i in range(0, len(sequence_2k)/2, 2):
        # imported print from python 3 so that I'm able to use end=""
        print (sequence_2k[i], end="")
    print("\n")
    t -= 1