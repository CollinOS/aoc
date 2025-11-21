from pathlib import Path

# -------------------
# Config for this day
# -------------------
DAY = 1  # change this per file: 1, 2, 3, ...
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
    x = 0
    y = 0

    while (int(data[x]) + int(data[y]) != 2020):
      
        if y % (len(data)-1) == 0:
            x += 1
            y = 0

        y += 1       

    z = int(data[x]) * int(data[y])

    return z


def part2(data) -> int | str:
    x = 0
    y = 0
    z = 0

    while (int(data[x]) + int(data[y]) + int(data[z]) != 2020):
        
        z += 1

        if z >= len(data):
            z = 0
            y +=1
      
        if y >= len(data):
            y = 0
            x += 1               

    a = int(data[x]) * int(data[y]) * int(data[z])
    
    return a


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
