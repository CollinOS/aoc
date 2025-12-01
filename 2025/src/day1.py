from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 1  # change this per file: 1, 2, 3, ...
YEAR = 2025  # optional, just for reference/logging


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
    min = 0
    max = 99
    dial = 50
    hits = 0

    # first5 = data[:5]
    # print(first5)

    for x in data:
        direction, value = x[0], x[1:]
        value = int(value)

        if direction == "R":
            i = 0
            # print(dial, '+', value)

            while i < value:
                i += 1
                dial += 1
                if dial > max:
                    dial = min

            # print(dial)
            i = 0
        if direction == "L":
            i = 0
            # print(dial, '-', value)

            while i < value:
                i += 1
                dial -= 1
                if dial < min:
                    dial = max

            # print(dial)
            i = 0

        if dial == 0:
            hits += 1   
    
    return hits


def part2(data) -> int | str:
    min = 0
    max = 99
    dial = 50
    hits = 0

    # first5 = data[:5]
    # print(first5)

    for x in data:
        direction, value = x[0], x[1:]
        value = int(value)

        if direction == "R":
            i = 0
            # print(dial, '+', value)

            while i < value:
                i += 1
                dial += 1
                if dial > max:
                    dial = min
                    hits += 1

            # print(dial)
            i = 0
        if direction == "L":
            i = 0
            # print(dial, '-', value)

            while i < value:
                i += 1
                dial -= 1
                if dial == min:
                    hits += 1
                if dial < min:
                    dial = max

            # print(dial)
            i = 0 
    
    return hits


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
