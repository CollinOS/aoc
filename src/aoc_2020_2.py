from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 2  # change this per file: 1, 2, 3, ...
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
    count = 0

    for x in data: 
        # x = the current item in data being iterated
        # y has [0, 1, 2] of x
        # [0] = min-max amount of times value can appear in [2]
        # [1] = character to look for in [2]
        y = x.split(" ")
        min = int(y[0].split("-")[0])
        max = int(y[0].split("-")[1])
        char = x.split(":")[0][-1]
        pw = x.split()[-1]
        
        if (min <= pw.count(char) <= max):
            count += 1

    return count


def part2(data) -> int | str:
    count = 0

    for x in data: 
        # x = the current item in data being iterated
        # y has [0, 1, 2] of x
        # a & b = potential index for char
        """index 0 is now 1"""

        y = x.split(" ")
        a = int(y[0].split("-")[0])
        b = int(y[0].split("-")[1])
        char = x.split(":")[0][-1]
        pw = x.split()[-1]
        split_pw = list(pw)

        # check spots a & b (+1) of split_pw
        # if only one is true +1
        # c s c f g h
        # 1 2 3 4 5 6
        # 0 1 2 3 4 5
        if (split_pw[a-1] == char and split_pw[b-1] == char):
            count = count
        elif (split_pw[a-1] != char and split_pw[b-1] != char):
            count = count
        else:
            count += 1

    return count


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
