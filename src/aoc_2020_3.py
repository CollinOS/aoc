from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 3  # change this per file: 1, 2, 3, ...
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
    # repeat to the right until it reaches a y axis greater than the length
    # don't need to repeat can just jump down like
    """
    X      (0,0)
      X    (3,1)
        X  (6,2)
    X      (0,3)
      X    (3,4)
        X  (6,5)
    """
    x = 0
    y = 0
    length = len(data)
    trees = 0
    while y < (length-1):
        # need to handle first iteration where y = 0
        if y == 0:
            if (data[y])[0] == '#':
                trees += 1

        # this conditional feels a little redundant
        if ((x + 3) < len(data[y])):
            y += 1
            x += 3
        else:
            y += 1
            x = (x + 3) - len(data[y])

        # need to tell it to look at item y of data, and check character in pos X
        row = list(data[y])

        if (row[x] == '#'):
            trees += 1

    return(trees)


def part2(data) -> int | str:
    x = 0
    y = 0
    length = len(data)
    trees = 0
    mult_trees = 1


    right = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    i = 0

    while y < (length-1) and i < (len(right)):
        # need to handle first iteration where y = 0
        if y == 0:
            if (data[y])[0] == '#':
                trees += 1

        # this conditional feels a little redundant
        if ((x + right[i]) < len(data[y])):
            y += down[i]
            x += right[i]
        else:
            y += down[i]
            x = (x + right[i]) - len(data[y])

        # need to tell it to look at item y of data, and check character in pos X
        row = list(data[y])

        if (row[x] == '#'):
            trees += 1

        if (y == length-1):
            i += 1
            x = 0
            y = 0
            mult_trees *= trees
            trees = 0

    return(mult_trees)


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
