from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 2  # change this per file: 1, 2, 3, ...
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
    """
    invalid if any number or sequence of numbers repeat
    split number in half as a string, and if [0] == [1] the add it: invalid += duplicate
    add all invalid IDs together
    """
    invalid = 0
    low = 0
    high = 0
    
    """
    Solve part 1.
    """
    # TODO: before you start, change DAY at the top to match the day of the problem
    return 0


def part2(data) -> int | str:
    """
    Solve part 2.
    """
    # TODO: implement
    return 0


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
