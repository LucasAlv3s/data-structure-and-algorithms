'''
Example Basic
'''
from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

print(stack)

"""
Example POP
"""
from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

top_item =  stack.pop() # C
top_item = stack.pop() # B
top_item = stack.pop() # A

print(stack, top_item)

"""
Example Iterations and copy
"""
from typing import List
from copy import deepcopy

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

print('FOR: ')
for item in stack[::-1]:
    print(item)

# copy
stack_copy = deepcopy(stack)

print('\nWHILE: ')
while stack_copy:
    item = stack_copy.pop()
    print(item)
