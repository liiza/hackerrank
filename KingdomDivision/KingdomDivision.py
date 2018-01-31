#!/bin/python3

# Note: This only brings 48.33 points.
# One test case fails for maximum recursion depth exceeded.
# Perhaps full points could be achieved by porting this solution c++ 
# or some other language where the function stack is lighter.

import sys

three = {}
cache = {}

def ways_to_divide(node, parent, parent_same_color):
    if (node, parent_same_color) in cache:
        return cache[(node, parent_same_color)]

    children = [
        child for child in three[node]
        if child != parent
    ]
    
    if not children:
        # When node has no children, the node and child must always be same color
        cache[(node, True)] = 1
        cache[(node, False)] = 0
        return cache[(node, parent_same_color)]
    else:
        total = 1
        all_children_different_than_node = 1
        for child in children:
            # Each child can be either same color or different color than node
            total *= (
                ways_to_divide(child, node, False)
                +
                ways_to_divide(child, node, True)
            )
            all_children_different_than_node *= (
                ways_to_divide(child, node, False)
            )

        # If the node and the parent are same color, all the combinations of the children are allowed
        cache[(node, True)] = total
        # If the node and the parent are different colors, 
        # at least one of the childen must be the same color than node
        cache[(node, False)] = total - all_children_different_than_node

        return cache[(node, parent_same_color)]

def kingdomDivision(n, roads):
    for road in roads:
        neighbours = three.setdefault(road[0], [])
        neighbours.append(road[1])        
        neighbours = three.setdefault(road[1], [])
        neighbours.append(road[0])

    # There are equally many ways to divide the tree whether the root node is blue or red.
    # To get the total ways to divide multiple the ways_to_divide result by two.
    return (ways_to_divide(1, None, False) * 2) % (pow(10, 9) + 7)
        
if __name__ == "__main__":
    n = int(input().strip())
    roads = []
    for roads_i in range(n-1):
       roads_t = [int(roads_temp) for roads_temp in input().strip().split(' ')]
       roads.append(roads_t)
    result = kingdomDivision(n, roads)
    print(result)

