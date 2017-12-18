# https://www.hackerrank.com/challenges/almost-sorted/problem
_ = input()
nums = [int(i) for i in input().split(' ')]

holes = []
hills = []

"""
      *
     **
  *  **
  ** **
  *****
 ******
*******
0234567

hill at 3
hole at 5
-> Can be reversed
"""

for i in range(1, len(nums) - 1):
    if nums[i - 1] > nums[i] < nums[i + 1]:
        holes.append(i)
    elif nums[i - 1] < nums[i] > nums[i + 1]:
        hills.append(i)
        
if nums[0] > nums[1]:
    hills.append(0)
if nums[-1] < nums[-2]:
    holes.append(len(nums) - 1)

if len(hills) == 1 and len(holes) == 1:
    if (
            (
                (holes[0] + 1 == len(nums)) or (nums[hills[0]] < nums[holes[0] + 1])
            )
            and 
            (
                (hills[0] == 0) or (nums[holes[0]] > nums[hills[0] - 1])
            )
        ):
        print('yes')
        if holes[0] - hills[0] == 1:
            print('swap', hills[0] + 1, holes[0] + 1)
        else:
            print('reverse', hills[0] + 1, holes[0] + 1)
    else:
        print('no')
elif len(hills) == 2 and len(holes) == 2:
    if (
        (
            (holes[1] + 1 == len(nums)) or (nums[hills[0]] < nums[holes[1] + 1])
        )
        and 
        (
            (holes[1] == 0) or (nums[hills[0]] > nums[holes[1] - 1])
        )
        and 
        (
            (hills[0] + 1 == len(nums)) or (nums[holes[1]] < nums[hills[0] + 1])
        )
        and 
        (
            (hills[0] == 0) or (nums[holes[1]] > nums[hills[0] - 1])
        )
    ):
        print('yes')
        print('swap', hills[0] + 1, holes[1] + 1)
    else:
        print('no')
else:
    print('no')
