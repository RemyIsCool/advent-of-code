from dataclasses import dataclass


@dataclass
class Reindeer:
    rest_time: int
    speed: int
    burst_length: int
    points: int = 0
    distance: int = 0
    resting: bool = False
    cycle_counter: int = 0


with open("input.txt", "r") as f:
    reindeer_list: list[str] = f.readlines()


reindeers: list[Reindeer] = []


for line in reindeer_list:
    words = line.split()
    speed = int(words[3])
    burst_length = int(words[6])
    rest_time = int(words[-2])

    reindeers.append(Reindeer(rest_time, speed, burst_length))


for s in range(1, 2503):
    for reindeer in reindeers:
        if reindeer.resting:
            if reindeer.cycle_counter >= reindeer.rest_time:
                reindeer.cycle_counter = 0
                reindeer.resting = False
                reindeer.distance += reindeer.speed
        else:
            if reindeer.cycle_counter >= reindeer.burst_length:
                reindeer.cycle_counter = 0
                reindeer.resting = True
            else:
                reindeer.distance += reindeer.speed

        reindeer.cycle_counter += 1

    max_distance = max(reindeers, key=lambda r: r.distance).distance
    for reindeer in reindeers:
        if reindeer.distance == max_distance:
            reindeer.points += 1


print(max(reindeers, key=lambda r: r.points).points)
