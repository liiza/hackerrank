#!/bin/python3
#https://www.hackerrank.com/challenges/sherlock-and-cost/problem

import sys


def cost(arr):
    """We alternate between hills and dips to result into max difference."""

    hill = 0
    dip = 0
    
    for i in range(1, len(arr)):
        dip_hill = dip + abs(1 - arr[i])
        hill_hill = hill + abs(arr[i - 1] - arr[i])
        hill_dip = hill + abs(arr[i - 1] - 1)
        
        hill = max(dip_hill, hill_hill)
        # Dip-dip is never part of suboptimal solution
        dip = hill_dip
    
    return max(hill, dip)

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = cost(arr)
        print(result)

