def factorial(num: int) -> int:
    if num == 1:
        return 1
    # recursive case
    return num * factorial(num - 1)

if __name__ == '__main__':
    factorial5 = factorial(5)
print(factorial5)