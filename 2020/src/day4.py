
import re
from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 4  # change this per file: 1, 2, 3, ...
YEAR = 2020  # optional, just for reference/logging


# -------------------
# Input handling
# -------------------
def get_input_path(test: bool = False) -> Path:
    """
    Returns the Path to this day's input file.
    If test=True, looks for a ...-test.txt file (optional).
    """
    base_dir = Path(__file__).resolve().parents[1]  # project root (one level above src/)
    suffix = "-test" if test else ""
    return base_dir / "inputs" / f"day{DAY:02d}{suffix}.txt"


def read_input(test: bool = False) -> str:
    """
    Reads the raw input text for this day.
    """
    path = get_input_path(test=test)
    return path.read_text(encoding="utf-8").rstrip("\n")


# -------------------
# Parsing & solutions
# -------------------
def parse(raw: str):
    """
    Turn the raw input string into a useful data structure.
    Adjust this per day.
    """
    # Example default: split into lines
    return raw.splitlines()


def part1(data) -> int | str:
    valid = 0
    joined_list = "\n".join(data)
    split_list = joined_list.split("\n\n")
    passports = [s.replace("\n", " ") for s in split_list]
    required_fields = ["iyr:", "hgt:", "byr:", "pid:", "eyr:", "hcl:", "ecl:"]
    for p in passports:
        if all(field in p for field in required_fields):


            valid += 1
    return valid


def part2(data) -> int | str:
    valid = 0
    joined_list = "\n".join(data)
    split_list = joined_list.split("\n\n")
    passports = [s.replace("\n", " ") for s in split_list]
    required_fields = ["iyr:", "hgt:", "byr:", "pid:", "eyr:", "hcl:", "ecl:"]
    for p in passports:
        if all(field in p for field in required_fields):
            passport_fields = p.split(" ")
            check = 0
            for f in passport_fields:
                key, value = f.split(":")
                if key == "byr" and 1920 <= int(value) <= 2002:
                    check += 1
                if key == "iyr" and 2010 <= int(value) <= 2020:
                    check += 1
                if key == "eyr" and 2020 <= int(value) <= 2030:
                    check += 1
                if key == "hgt":
                    split = re.split(r"(?<=[0-9])(?=[A-Za-z])", value)
                    if len(split) == 2:
                        if split[1] == "cm" and int(split[0]) >= 150 and int(split[0]) <= 193:
                            check += 1
                        if split[1] == "in" and int(split[0]) >= 59 and int(split[0]) <= 76:
                            check += 1
                if key == "hcl" and re.fullmatch(r"#[0-9a-f]{6}", value):
                    check += 1
                if key == "ecl" and value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
                    check += 1
                if key == "pid" and all(x in "0123456789" for x in value) and len(value) == 9:
                    check += 1
            if check == len(required_fields):
                valid += 1

    return valid


# -------------------
# CLI entrypoint
# -------------------
def main() -> None:
    raw = read_input(test=False)
    data = parse(raw)

    print(f"Advent of Code {YEAR} - Day {DAY:02d}")
    print("-" * 30)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
