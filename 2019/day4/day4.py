def is_valid_password(password):
    password = str(password)

    has_double = False
    increasing = True
    groups = {}

    for i in range(5):
        if password[i] > password[i + 1]:
            increasing = False
            break

        groups[password[i]] = groups.get(password[i], 0) + 1

    groups[password[5]] = groups.get(password[5], 0) + 1

    has_double = any(count == 2 for count in groups.values())

    return has_double and increasing


def count_valid_passwords(start, end):
    return sum(1 for pw in range(start, end + 1) if is_valid_password(pw))


start_range = 158126
end_range = 624574

result = count_valid_passwords(start_range, end_range)
print("Valid Passwords:", result)
