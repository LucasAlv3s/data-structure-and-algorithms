# Example One:

'''
import sys
sys.setrecursionlimit(5000)

def factorial(num: int) -> int:
    # base case
    if num == 1:
        return 1
    # recursive case
    return num * factorial(num - 1)

if __name__ == '__main__':
    factorial5 = factorial(5)
print(factorial5)
'''

# Example Two:

from typing import List
from collections import namedtuple

Cashier = namedtuple('Cashier', 'find_key')

def find_key(cashier: List[Cashier], index: int = 0) -> Cashier:
    # base case
    if len(boxes) <= index:
        return Cashier(False)
    
    cashier = boxes[index]

    # base case
    if cashier.find_key:
        return Cashier

    # recursive case    
    index += 1
    return find_key(boxes, index)

if __name__ == '__main__':
    boxes: List[Cashier] = [
        Cashier(False), Cashier(False), Cashier(False),
        Cashier(False), Cashier(False), Cashier(False),
        Cashier(False), Cashier(True), Cashier(False),
        Cashier(False), Cashier(False), Cashier(False),
    ]

print(find_key(boxes))
