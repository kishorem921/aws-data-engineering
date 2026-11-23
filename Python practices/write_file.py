from pathlib import Path

file_path = Path(__file__).parent / "input.txt"
output_file = Path(__file__).parent / "output.txt"

with open(file_path, "r") as in_f:
    with open(output_file, "w") as out_f:
        for line in in_f:
            cleaned_names = line.strip().upper()
            out_f.write(cleaned_names + "\n")

print("File written successfully")

