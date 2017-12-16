#!/bin/python3
# The Grid search

import sys
import re

t = int(input().strip())
for a0 in range(t):
	R,C = input().strip().split(' ')
	R,C = [int(R),int(C)]
	G = []
	G_i = 0
	for G_i in range(R):
	   G_t = str(input().strip())
	   G.append(G_t)
	r,c = input().strip().split(' ')
	r,c = [int(r),int(c)]
	P = []
	P_i = 0
	for P_i in range(r):
	   P_t = str(input().strip())
	   P.append(P_t)
	   
	matching_sub_matrix = False

	for y in range(R-r+1):
		for x in range(C-c+1):
			matches = True
			for i_row, row in enumerate(P): 
				if not matches:
					break
				for i_num, num in enumerate(row):
					if num != G[y + i_row][x + i_num]:
						matches = False
						break
			matching_sub_matrix = matches or matching_sub_matrix

	if matching_sub_matrix:
		print('YES')
	else:
		print('NO')
			