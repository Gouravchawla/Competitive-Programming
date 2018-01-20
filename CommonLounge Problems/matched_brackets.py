#!/usr/bin/env python

"""
Source: https://www.codechef.com/ZCOPRAC/problems/ZCO12001
"""


def main():
    pattern_length = input()
    pattern = map(int, raw_input().split())
    max_nesting = {'depth': 0, 'pos': 0}
    max_pattern = {'length': 0, 'pos': 0}
    stack = []
    counter = 0
    nesting_pos = 0
    pattern_pos = 0

    # Base case
    if pattern_length == 2:
        print 1, 1, 2, 1

    else:
        for i in range(pattern_length):
            stack_len = len(stack)
            # Push into stack whenever there is 1 i.e. '('
            if pattern[i] == 1:
                # The pattern starts when stack is empty and we are about to
                # push an element in the stack
                if stack_len == 0:
                    # temp variable to help us find maximum length pattern
                    # start position
                    pattern_pos = i+1
                # temp variable to help us find maximum depth pattern start pos
                nesting_pos = i+1
                stack.append(pattern[i])
                counter += 1
            else:
                # if max depth is less than stack length then only we
                # update the max depth since we want the first occurence only
                if max_nesting['depth'] < stack_len:
                    max_nesting = {'depth': stack_len, 'pos': nesting_pos}
                stack.pop()
                counter += 1
                if stack_len == 1:
                    # if max pattern length < counter then only we update
                    # the max length since we want the first occurence
                    if max_pattern['length'] < counter:
                        max_pattern = {
                            'length': counter, 'pos': pattern_pos
                        }
                    counter = 0
        print max_nesting['depth'], max_nesting['pos'], max_pattern['length'],\
            max_pattern['pos']


if __name__ == '__main__':
    main()
