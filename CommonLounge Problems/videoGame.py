#!/usr/bin/env python

'''
Source: https://www.codechef.com/ZCOPRAC/problems/ZCO14001
'''

from __future__ import print_function


def process_command(i, N, H, crane, position, current_formation ):
    if i == '1': # Move Left
        if position == 0:
            pass
        else:
            position -= 1
    elif i == '2': # Move Right
        if position == N-1:
            pass
        else:
            position += 1
    elif i == '3': # Pick up
        if crane == 0:
            if current_formation[position] > 0:
                crane = 1
                current_formation[position] -= 1
        else:
            pass
    elif i == '4': # Drop down
        if crane == 1:
            if current_formation[position] >= H:
                pass
            else:
                current_formation[position] += 1
                crane = 0
        else:
            pass
    else: # End of first outer if
        pass
    return position, crane, current_formation

def main():
    N, H = map(int, raw_input().split())
    initial_formation = map(int, raw_input().split())
    commands = raw_input()
    current_formation = initial_formation
    position = 0
    crane = 0
    for i in commands:
        position, crane, current_formation = process_command(i, N, H, crane, position, current_formation)

    for i in current_formation:
        print(i, end=' ')


if __name__ == '__main__':
    main()
