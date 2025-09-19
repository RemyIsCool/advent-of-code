from string import ascii_lowercase as alphabet


with open("input.txt", "r") as f:
    current_password: str = f.read()


def increment_password(password: str) -> str:
    if len(password) == 0:
        return alphabet[1]
    last_letter: str = password[-1]
    next_index: int = alphabet.index(last_letter) + 1
    if next_index >= len(alphabet):
        next_index = 0
        return increment_password(password[:-1]) + alphabet[0]

    return password[:-1] + alphabet[next_index]


def matches_requirements(password: str) -> bool:
    incrementing_letters = any(
        map(lambda x: alphabet[x : x + 3] in password, range(len(alphabet) - 2))
    )
    banned_letters = all(map(lambda c: c not in password, "iol"))

    double_count = 0
    for letter in alphabet:
        if letter * 2 in password:
            double_count += 1

    two_doubles = double_count >= 2

    return incrementing_letters and banned_letters and two_doubles


while not matches_requirements(current_password):
    current_password = increment_password(current_password)

print(current_password)
current_password = increment_password(current_password)

while not matches_requirements(current_password):
    current_password = increment_password(current_password)

print(current_password)
