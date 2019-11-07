#!/usr/bin/env python3

import operator
import sys
import argparse

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg, debug_mode=False):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        if debug_mode:
            print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')
    options = parser.parse_args()
    while True:
        result = calculate(input("rpn calc> "), debug_mode=options.debug)
        print("Result: ", result)

if __name__ == '__main__':
    main()
