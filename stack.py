from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')

top_item =  stack.pop() # C

print(stack, top_item)
