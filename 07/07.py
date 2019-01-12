#! /usr/bin/env python3

from string import ascii_uppercase

class Worker:
    time_remaining = 0
    current_job = None
    def is_done(self):
        return self.time_remaining <= 0
    def decrement(self):
        self.time_remaining -= 1
    def assign_job(self, job):
        self.current_job = job
        self.time_remaining = ord(job) - 4
    def finish_job(self):
        self.current_job = None

def find_next_step(dependencies):
    return min(dependencies.items(), key=lambda x: (len(x[1]), x[0]))[0]

def singleWorker(dependencies):

    order = []
    total_letters = len(dependencies.keys())

    while len(order) < total_letters:
        next_step = find_next_step(dependencies)
        dependencies.pop(next_step)
        for key in dependencies.keys():
            if next_step in dependencies[key]:
                dependencies[key].remove(next_step)
        order.append(next_step)

    print('Part A: {}'.format(''.join(order)))
    # Part A: BKCJMSDVGHQRXFYZOAULPIEWTN

def fiveWorkers(dependencies):
    order = []
    seconds = 0
    workers = [Worker() for _ in range(5)]
    total_letters = len(dependencies.keys())

    while len(order) < total_letters:
        for worker in workers:
            if worker.is_done():

                # Finish the current job
                if worker.current_job:
                    order.append(worker.current_job)
                    for key in dependencies.keys():
                        if worker.current_job in dependencies[key]:
                            dependencies[key].remove(worker.current_job)
                    worker.finish_job()

                # Start the next job if there is one
                if dependencies.items():
                    next_step = find_next_step(dependencies)
                    if dependencies[next_step] == set():
                        worker.assign_job(next_step)
                        dependencies.pop(next_step)

        seconds += 1
        for worker in workers:
            worker.decrement()

    print('Part B: {}'.format(seconds - 1))
    #Part B: 1040

if __name__ == "__main__":
    file = open('./input.txt', 'r').read().splitlines()
    steps = [tuple((line.split(' ')[1], line.split(' ')[7])) for line in file]
    dependencies = {}

    for letter in ascii_uppercase:
        dependencies[letter] = set()

    for (cause, effect) in steps:
        dependencies[effect].add(cause)

    # singleWorker(dependencies)
    fiveWorkers(dependencies)
