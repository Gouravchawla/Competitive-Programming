# URL: http://www.spoj.com/problems/CPTTRN3/
from __future__ import print_function


t = input()

while t:
    l, c = raw_input().split(" ")
    l = int(l)
    c = int(c)

    for i in range(0, (3*l)+1):
        for j in range(0, (3*c)+1):
            if i in range(0, (3*l)+1, 3):
                print('*', end="")
            elif j in range(0, (3*c)+1, 3):
                print('*', end="")
            else:
                print('.', end="")
        print("\n")
    t -= 1
