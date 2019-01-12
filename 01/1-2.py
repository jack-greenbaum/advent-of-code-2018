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

file = open('./frequencies.txt', 'r')
frequencies = file.read().splitlines()

print(find_duplicate(frequencies))
# Answer: 66932