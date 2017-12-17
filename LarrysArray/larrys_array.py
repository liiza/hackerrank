# https://www.hackerrank.com/challenges/larrys-array/problem
test_cases = int(input())
for test_case in range(test_cases):
    _ = input()
    permutation = [int(num) for num in input().split(' ')]
    inversions = 0

    for i, num in enumerate(permutation):
        for j in range(i+1, len(permutation)):
            if num > permutation[j]:
                inversions += 1
                
    if inversions % 2 == 0:
        print('YES')
    else: 
        print('NO')
        
