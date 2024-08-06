import re

strings = ["b", "ab", "bba"]
pattern = "b$"

# compiled = re.compile(pattern)

for string in strings:
    print(f"{string}\t", "Matched" if re.match(pattern,string) else "No Match")