from itertools import permutations


with open("input.txt", "r") as f:
    seating_preferences = f.readlines()

people: set[str] = {"You"}
preferences: dict[tuple[str, str], int] = {}

for line in seating_preferences:
    words: list[str] = line.split()
    person: str = words[0]
    amount: int = int(words[3]) * (-1 if words[2] == "lose" else 1)
    neighbor: str = words[-1][:-1]

    preferences[(person, neighbor)] = amount

    people.add(person)

for person in people:
    preferences[(person, "You")] = 0
    preferences[("You", person)] = 0


scores: list[int] = []

for arrangement in permutations(people):
    score = 0
    for x in range(len(arrangement)):
        person = arrangement[x]
        before = arrangement[(x - 1) % len(arrangement)]
        after = arrangement[(x + 1) % len(arrangement)]

        score += preferences[(person, before)] + preferences[(person, after)]
    scores.append(score)

print(max(scores))
