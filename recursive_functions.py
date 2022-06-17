# import sys
# sys.setrecursionlimit(5000)

def factorial(num: int) -> int:
    # base case
    if num == 1:
        return 1
    # recursive case
    return num * factorial(num - 1)

if __name__ == '__main__':
    factorial5 = factorial(5)
print(factorial5)