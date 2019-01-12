from collections import defaultdict

def editDistance(first, second):
    mistakes_allowed = 1
    bad_char = None
    for i in range(0, len(first)):
        if first[i] != second[i]:
            if mistakes_allowed:
                mistakes_allowed -= 1
                bad_char = i
            else:
                return False
    print (first[:bad_char] + first[(bad_char + 1):])
    return True

def solve(boxes):
    for box1 in boxes:
        for box2 in boxes:
            if box1 != box2:
                if editDistance(box1, box2):
                    return

file = open('./boxes.txt', 'r')
boxes = file.read().splitlines()
solve(boxes)
# Answer: cypueihajytordkgzxfqplbwn
