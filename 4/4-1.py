from collections import defaultdict
import re

def calc_sleep_times(sorted_times):
    guards = defaultdict(lambda: [0 for x in range(60)])
    current_guard = None
    bedtime = None

    for (year, month, day, hour, minute, last) in sorted_times:
        if (last == 'asleep'):
            bedtime = int(minute)
            continue
        elif (last == 'up'):
            for x in range(bedtime, int(minute)):
                guards[current_guard][x] += 1
            bedtime = None
            continue
        else:
            current_guard = int(last)

    sleepiest_guard = max(guards.items(), key = lambda x: sum(guards[x]))
    sleepiest_minute = guards[sleepiest_guard].index(max(guards[sleepiest_guard]))
    print('Part A: {}'.format(sleepiest_guard * sleepiest_minute))

    consistent_guard = max(guards, key = lambda x: max(guards[x]))
    consistent_minute = guards[consistent_guard].index(max(guards[consistent_guard]))
    print('Part B: {}'.format(consistent_guard * consistent_minute))

file = open('guards.txt', 'r')
timestamps = file.read().splitlines()
sorted_times = sorted(map(lambda s: re.findall(r'\d+|(?![shift])[A-Za-z]+$', s), timestamps), key = lambda x: (x[1], x[2], x[3], x[4]))
calc_sleep_times(sorted_times)
# Part A: 11367
# Part B: 1153
