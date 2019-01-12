from collections import defaultdict
import re

file = open('./rectangles.txt', 'r')
rectangles = file.read().splitlines()
plans = map(lambda s: map(int, re.findall(r'-?\d+', s)), rectangles)

spaces = defaultdict(list)
overlaps = {}

for (cid, xcord, ycord, width, height) in plans:
    overlaps[cid] = set()
    for i in range(xcord, xcord + width):
        for j in range (ycord, ycord + height):
            if spaces[(i,j)]:
                for num in spaces[(i, j)]:
                    overlaps[num].add(cid)
                    overlaps[cid].add(num)
            spaces[(i,j)].append(cid)

print ('Part 1: {0}'.format(len([k for k in spaces if len(spaces[k]) > 1]))) # Answer: 113576
print ('Part 2: {0}'.format([x for x in overlaps if len(overlaps[x]) == 0][0])) #Answer: 825