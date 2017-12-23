#!/bin/python3
#https://www.hackerrank.com/challenges/candies/problem

import sys

def candies(n, arr):
    candies = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i + 1] + 1, candies[i])

    return sum(candies)

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
       arr_t = int(input().strip())
       arr.append(arr_t)
    result = candies(n, arr)
    print(result)

