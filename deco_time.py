#!/usr/bin/env python





def factorial(num):
    result = num
    while(num != 1):
        result = result * (num-1)
        num = num-1
    return result


if __name__ == '__main__':
    print(factorial(6))




