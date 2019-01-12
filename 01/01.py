#! /usr/bin/env python3

from itertools import accumulate

def net_frequency(frequencies):
    data = [int(frequency) for frequency in frequencies]
    return list(accumulate(data))[-1]

def find_duplicate(frequencies):
    current = 0
    seen_totals = set()

    # We may need to loop through the list more than once
    while (True):
        for frequency in frequencies:
            current += int(frequency)
            if current in seen_totals:
                return current
            seen_totals.add(current)

if __name__ == "__main__":
    file = open('./input.txt', 'r')
    frequencies = file.read().splitlines()
    print('Part 1: {}'.format(net_frequency(frequencies)))
    print('Part 2: {}'.format(find_duplicate(frequencies)))