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

file = open('./boxes.txt', 'r')
boxes = file.read().splitlines()
duplicates = find_doubles_and_triples(boxes)
print(duplicates['doubles'] * duplicates['triples'])
# Answer: 5166