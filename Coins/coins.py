#!/bin/python3
# https://www.hackerrank.com/challenges/coin-change/problem

import sys

def getWays(n, coins):
    coins = sorted(coins)
    # + 1 is for including zeros
    ways = [[0] * (n + 1) for i in range(len(coins) + 1)]
    for i in range(0, n + 1):
        for j in range(len(coins) + 1):
            
            if i == 0:
                ways[j][i] = 1
                continue

            if j == 0:
                ways[j][i] = 0
                continue

            c = coins[j - 1]

            if i < c:
                ways[j][i] = ways[j - 1][i]
                continue

            ways[j][i] += (ways[j - 1][i] + ways[j][i - c])

    return ways[len(coins)][n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)







