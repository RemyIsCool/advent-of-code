from json import load
from typing import Any


with open("input.txt", "r") as f:
    json: dict[str, Any] = load(f)


def check_value(value: Any) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        count = 0
        for key, value in value.items():
            if value == "red":
                return 0
            count += check_value(value)
        return count
    if isinstance(value, list):
        count = 0
        for item in value:
            count += check_value(item)
        return count
    return 0


print(check_value(json))
