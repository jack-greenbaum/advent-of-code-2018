#! /usr/bin/env python3

from collections import defaultdict

def find_doubles_and_triples(boxes):
    repeats = {'doubles': 0, 'triples': 0}
    for box in boxes:
        seen = defaultdict(int)
        for letter in box:
            seen[letter] += 1
        if 2 in seen.values():
            repeats['doubles'] += 1
        if 3 in seen.values():
            repeats['triples'] += 1
    return repeats

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
    print('Part 2: {}'.format((first[:bad_char] + first[(bad_char + 1):])))
    return True

def solve(boxes):
    for box1 in boxes:
        for box2 in boxes:
            if box1 != box2:
                if editDistance(box1, box2):
                    return

if __name__ == "__main__":
    file = open('./input.txt', 'r')
    boxes = file.read().splitlines()
    duplicates = find_doubles_and_triples(boxes)
    print('Part 1: {}'.format(duplicates['doubles'] * duplicates['triples']))
    solve(boxes)