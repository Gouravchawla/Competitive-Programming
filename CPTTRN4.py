# URL: http://www.spoj.com/problems/CPTTRN4/
from __future__ import print_function

t = input()

while t:

    inputVar = [eval(x) for x in raw_input().split()]

    for i in range(0, ((inputVar[2]+1)*inputVar[0])+1):
        for j in range(0, ((inputVar[3]+1)*inputVar[1])+1):
            if i in range(0, ((inputVar[2]+1)*inputVar[0])+1, inputVar[2]+1):
                print('*', end="")
            elif j in range(0, ((inputVar[3]+1)*inputVar[1])+1, inputVar[3]+1):
                print('*', end="")
            else:
                print('.', end="")
        print("\n")
    t -= 1
