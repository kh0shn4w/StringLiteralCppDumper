import json
import string

with open("stringliteral.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def is_printable(s):
    printable = sum(c in string.printable for c in s)
    return printable / max(len(s), 1) > 0.7

filtered = [entry for entry in data if is_printable(entry["value"])]

with open("readable_strings.txt", "w", encoding="utf-8") as out:
    for entry in filtered:
        out.write(f'{entry["address"]}: {entry["value"]}\n')

print(f"Extracted {len(filtered)} readable strings → check readable_strings.txt")

