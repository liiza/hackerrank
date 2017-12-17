# https://www.hackerrank.com/challenges/encryption/problem
import sys
import math

s = input().strip()
l = len(s)

floor = math.floor(l)
ceil = math.ceil(l)

row = min(floor, ceil)
column = max(floor, ceil)

encrypted = [""] * row

for index, c in enumerate(s):
     encrypted[index%row] += c


print(" ".join(encrypted))
