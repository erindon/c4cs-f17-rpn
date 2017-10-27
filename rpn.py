#!/usr/bin/env python3

import operator

def subtract (a,b):
        return a - b
def add (a,b):
        return a + b
ops = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
                        stack.append(int(token))
		except ValueError:
                        arg1 = stack.pop()
                        arg2 = stack.pop()
                        function = ops[token]
                        result =  function(arg2, arg1)
                        stack.append(result)
#	print(stack)
	return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
    

