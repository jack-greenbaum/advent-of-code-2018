from itertools import cycle

class Player:
    def __init__(self):
        self.score = 0

class Marble:
    def __init__(self, value):
        self.value = value
        self.clockwise = self
        self.counter_clockwise = self

def place(current_marble, new_marble):
    counter_clockwise_neighbor = current_marble.clockwise
    clockwise_neighbor = current_marble.clockwise.clockwise
    counter_clockwise_neighbor.clockwise = new_marble
    clockwise_neighbor.counter_clockwise = new_marble
    new_marble.counter_clockwise = counter_clockwise_neighbor
    new_marble.clockwise = clockwise_neighbor

def remove_seven_counter_clockwise(current_marble):
    to_remove = current_marble\
                    .counter_clockwise\
                    .counter_clockwise\
                    .counter_clockwise\
                    .counter_clockwise\
                    .counter_clockwise\
                    .counter_clockwise\
                    .counter_clockwise
    to_remove.counter_clockwise.clockwise = to_remove.clockwise
    to_remove.clockwise.counter_clockwise = to_remove.counter_clockwise
    return (to_remove.value, to_remove.clockwise)

def play(num_players, marbles):
    players = [Player() for _ in range(num_players)]
    player_itr = cycle(players)
    current_marble = Marble(0)
    for marble in marbles:
        current_player = next(player_itr)
        if (marble % 23 != 0):
            new_marble = Marble(marble)
            place(current_marble, new_marble)
            current_marble = new_marble
        else:
            removed_marble, current_marble = remove_seven_counter_clockwise(current_marble)
            current_player.score += marble + removed_marble
    return max([player.score for player in players])



description = open('./description.txt').read().split(' ')
num_players, num_marbles = int(description[0]), int(description[6])
print('Part A: {}'.format(play(num_players, [x + 1 for x in range(num_marbles)])))
print('Part B: {}'.format(play(num_players, [x + 1 for x in range(num_marbles * 100)])))