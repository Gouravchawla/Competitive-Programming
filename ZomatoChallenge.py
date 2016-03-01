"""
Problem Name: Xenny and partially sorted strings
URL: https://www.hackerearth.com/problem/algorithm/xenny-and-partially-sorted-strings-7/description/
Author: Gourav Chawla
"""

T = eval(input())


for t in range(T):
    lstString = []
    lstNew = []
    N, K, M = map(int, input().split())

    for x in range(N):
        lstString.append(input())
        lstNew.append((lstString[x][0:M], x))

    # Sorting the list
    lstNew.sort()

    # lstString[lstNew[key to print in sorted list][key string in the original list]]
    print(lstString[lstNew[K-1][1]])
