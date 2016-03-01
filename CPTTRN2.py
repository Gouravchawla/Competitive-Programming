# URL: http://www.spoj.com/problems/CPTTRN2/
from __future__ import print_function


t = input()

while t:
    l, c = raw_input().split(" ")

    for i in range(int(l)):
        for j in range(int(c)):
            if i == 0 or i == int(l)-1:
                print ('*', end="")
            elif j == 0 or j == int(c)-1:
                print ('*', end="")
            else:
                print('.', end="")
        print("\n")
    t -= 1
