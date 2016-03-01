import sys
__author__ = 'Gourav Chawla'
"""
    Problem Code: INTEST
    Problem URL: http://www.codechef.com/problems/INTEST
    Compatability: Python 3.x
"""

n, k = input().split()
n = eval(n)
k = eval(k)

inputVar = 0
count = 0

# inputVar = [eval(x) for x in input().split()]

inputVar = list(map(int, sys.stdin.readlines()))

for i in inputVar:
   if i % k == 0:
       count += 1

print(count)

