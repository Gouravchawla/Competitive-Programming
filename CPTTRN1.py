# URL: http://www.spoj.com/problems/CPTTRN1/
from __future__ import print_function


t = input()

while t:
    l, c = raw_input().split(" ")

    for i in range(int(l)):
        for j in range(int(c)):
            if i%2 == 0:
                if j % 2 == 0:
                    print('*', end="")
                else:
                    print('.', end="")
            else:
                if j % 2 == 0:
                    print('.', end="")
                else:
                    print('*', end="")
        print("\n")
    t -= 1

# Optimized solution: http://www.lai18.com/content/621767.html
# t = int(input())
# str='*.'
# for i in range(t):
#     line = input();
#     l = int(line.split(' ')[0])
#     c = int(line.split(' ')[1])
#     for j in range(l):
#         for k in range(c):
#             print(str[int((j + k)%2)], sep='', end='')
#         print()