#! /usr/bin/env python3

from string import ascii_lowercase

def oppositePolarity(first, second):
    return first.swapcase() == second

def scan(polymer):
    stable = []
    for letter in polymer:
        if stable and oppositePolarity(stable[-1], letter):
            stable.pop()
        else:
            stable.append(letter)
    return len(stable)

if __name__ == "__main__":
    file = open('input.txt', 'r')
    polymer = file.read()

    print('Part A: {}'.format(scan(polymer)))
    print('Part B: {}'.format(min([scan(polymer.replace(letter, '').replace(letter.upper(), '')) for letter in ascii_lowercase])))
