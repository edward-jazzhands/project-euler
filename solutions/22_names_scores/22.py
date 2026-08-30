"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.
For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would 
obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
"""

from pathlib import Path

script_dir = Path(__file__).resolve().parent

def alphabet_value(name: str) -> int:

    total = 0
    for letter in name:
        score = ord(letter) - 64
        total += score
    return total


with open(f"{script_dir}/names.txt", "r") as f:
    # 46kb file we can load entirely into memory without issues
    big_str = f.read()

listed = big_str.replace('"', '').split(",")
listed.sort()

scores_total = 0
for i, name in enumerate(listed):
    a_val = alphabet_value(name)
    namescore = (i+1)*a_val
    scores_total += namescore

print(scores_total)