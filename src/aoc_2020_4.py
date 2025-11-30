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
            print(passport_fields)
            for f in passport_fields:
                check = 0
                if byr >= 1920 and byr <= 2002:
                    check += 1
                if iyr >= 2010 and iyr <= 2020:
                    check += 1
                if eyr >= 2020 and eyr <= 2030:
                    check += 1

                if checks == 6:
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
