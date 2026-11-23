from pathlib import Path

file_path = Path(__file__).parent / "input.txt"

with open(file_path, "r") as f:
    for line in f:
        print(line)

