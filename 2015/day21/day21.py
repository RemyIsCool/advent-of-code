from sys import stdin
from dataclasses import dataclass
from itertools import product, combinations
from copy import copy


@dataclass
class Entity:
    hp: int = 100
    damage: int = 0
    armor: int = 0


shop: dict[str, dict[str, tuple[int, int, int]]] = {
    "weapons": {
        "dagger": (8, 4, 0),
        "shortsword": (10, 5, 0),
        "warhammer": (25, 6, 0),
        "longsword": (40, 7, 0),
        "greataxe": (74, 8, 0),
    },
    "armor": {
        "leather": (13, 0, 1),
        "chainmail": (31, 0, 2),
        "splintmail": (53, 0, 3),
        "bandedmail": (75, 0, 4),
        "platemail": (102, 0, 5),
    },
    "rings": {
        "damage +1 ": (25, 1, 0),
        "damage +2 ": (50, 2, 0),
        "damage +3 ": (100, 3, 0),
        "defense +1": (20, 0, 1),
        "defense +2": (40, 0, 2),
        "defense +3": (80, 0, 3),
    },
}


boss: Entity = Entity()

for line in stdin:
    key, value_str = line.split(": ")
    value: int = int(value_str)

    match key:
        case "Hit Points":
            boss.hp = value
        case "Damage":
            boss.damage = value
        case "Armor":
            boss.armor = value


def simulate_fight(you_arg: Entity, boss_arg: Entity) -> bool:
    you = copy(you_arg)
    boss = copy(boss_arg)

    while you.hp > 0 and boss.hp > 0:
        boss.hp -= you.damage - boss.armor
        if boss.hp <= 0:
            break
        you.hp -= boss.damage - you.armor

    return you.hp > boss.hp


armors = []
for b in range(2):
    for combo in combinations(shop["armor"].values(), b):
        armors.append(combo)

rings = []
for c in range(3):
    for combo in combinations(shop["rings"].values(), c):
        rings.append(combo)

a = list(product(list(product(shop["weapons"].values(), armors)), rings))

wins = []
losses = []

for e in a:
    ((w_cost, w_damage, _), armors), rings = e

    total_cost = w_cost
    total_damage = w_damage
    total_armor = 0

    for cost, _, armor in armors:
        total_cost += cost
        total_armor += armor

    for cost, damage, armor in rings:
        total_cost += cost
        total_damage += damage
        total_armor += armor

    if simulate_fight(Entity(damage=total_damage, armor=total_armor), boss):
        wins.append(total_cost)
    else:
        losses.append(total_cost)

print(min(wins))
print(max(losses))
