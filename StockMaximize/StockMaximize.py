#!/bin/python3

# https://www.hackerrank.com/challenges/stockmax/problem

import sys

def max_profit(stocks):
	max_profit = 0
	max_so_far = 0
	for i in range(len(stocks) - 1, -1, -1):
		stock = stocks[i]
		if stock > max_so_far:
			max_so_far = stock
		max_profit += max_so_far - stock
	return max_profit

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		arr = list(map(int, input().strip().split(' ')))
		print(max_profit(arr))
