# URL: http://www.spoj.com/problems/CPTTRN4/
from __future__ import print_function
from datetime import datetime as dt

t = input()

while t:
    t1 = dt.now()
    inputVar = [eval(x) for x in raw_input().split()]
    dict_prime = {}

    for i in xrange(2, inputVar[0]+1):
        dict_prime[i] = True

    print("Original dict:", dict_prime)

    # From 2 to root of upper limit
    for i in xrange(2, int(inputVar[0]**0.5)+1):
        if dict_prime[i]:
            p = i
            for j in xrange(2*p, inputVar[0], p):
                dict_prime[j] = False
            print("New dict with multiples of {} removed: ".format(p), dict_prime)

    for i in xrange(2, inputVar[0]+1):
        if dict_prime[i]:
            print(i)
    t2 = dt.now()
    print("Time taken for Case #{} :".format(t), (t2-t1).microseconds/1e6)
    t -= 1
