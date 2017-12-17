# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
import sys

q = int(input().strip())
for a0 in range(q):
	n = int(input().strip())
	M = []
	for M_i in range(n):
	   M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
	   M.append(M_t)

	container_lens = []
	balls_lens = [0] * n
	for container in M:
		container_lens.append(len(container))
		for index, balls in enumerate(container):
			balls_lens[index] += balls

	if sorted(container_lens) == sorted(balls_lens):
		print('Possible')
	else:
		print('Impossible')


