__author__ = 'Gourav Chawla'
"""
    Problem Code: HS08TEST
    Problem URL : http://www.codechef.com/problems/HS08TEST
    Compatability: Python 3.x
"""

x,y = input().split()   # Splits the input into two strings. The space between strings acts as the delimiter
                        # and assigns those strings to the x and y respectively
                        # It is needed because input in online judges is space seperated i.e. 30 120.00

x = float(x)            # Parsing the string type default value to float
y = float(y)

# An alternate way of doing above things:
# m, n = [int(x) for x in input().split(' ')]


if x % 5 == 0 and x + 0.50 < y:
    print(format(y - (x + 0.50), '.2f'))
else:
    print(format(y, '.2f'))