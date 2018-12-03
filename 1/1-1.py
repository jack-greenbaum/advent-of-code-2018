from itertools import accumulate

def net_frequency(frequencies):
    data = [int(frequency) for frequency in frequencies]
    return list(accumulate(data))[-1]

file = open('./frequencies.txt', 'r')
frequencies = file.read().splitlines()

print(net_frequency(frequencies))
# Answer: 472