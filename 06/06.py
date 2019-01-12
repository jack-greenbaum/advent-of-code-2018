#! /usr/bin/env python3

from collections import defaultdict

def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

def is_out_of_bounds(point, max_x, max_y, min_x, min_y):
    return point[0] >= max_x or point[0] <= min_x or point[1] >= max_y or point[1] <= min_y

def largest_finite_area(points):
    matrix = {}
    buffer = int(10000 / len(points))
    min_x = min([point[0] for point in points])
    max_x = max([point[0] for point in points])
    min_y = min([point[1] for point in points])
    max_y = max([point[1] for point in points])
    region = set()

    for i in range(min_x - buffer, max_x + buffer):
        for j in range(min_y - buffer, max_y + buffer):
            distance_matrix = [((x, y), manhattan_distance((x, y), (i, j))) for x, y in points]
            distances = [distance for point, distance in distance_matrix]

            if sum(distances) < 10000:
                region.add((i, j))

            min_dist = min(distance_matrix, key=lambda d: d[1])
            matrix[(i, j)] = min_dist[0] if distances.count(min_dist[1]) == 1 else None

    counts = defaultdict(int)
    for (x, y), closest in matrix.items():
        if not closest:
            continue
        if is_out_of_bounds((x, y), max_x, max_y, min_x, min_y):
            counts[closest] -= 2 ** 31
        counts[closest] += 1

    print('Part A: {}'.format(max(counts.values())))
    print('Part B: {}'.format(len(region)))

if __name__ == "__main__":
    file = open('input.txt', 'r')
    points = list(map(lambda x: (int(x[0]), int(x[1])), [line.split(', ') for line in file.read().splitlines()]))
    print(largest_finite_area(points))