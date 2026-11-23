from pathlib import Path
input_file = Path(__file__).parent / "employees.txt"
output_file = Path(__file__).parent /"cleaned_employees.txt"

with open(input_file, 'r') as infile:
    with open(output_file, 'w') as outfile:
        for index, line in enumerate(infile, 1):
            cleaned_line = line.strip().upper()
            outfile.write(f"{index}: {cleaned_line}\n")

print("Pipeline completed successfully!")