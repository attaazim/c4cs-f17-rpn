#!/usr/bin/env python3

import operator
import readline
from termcolor import colored, cprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
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
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def dummy_func():
    dummy_number = 2
    dummy_string = "here is a dummy number: " + str(dummy_number)
    print(dummy_string)

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print_string = "Result: " + str(result)
        cprint(print_string, "red")

    dummy_func()

if __name__ == '__main__':
    main()
