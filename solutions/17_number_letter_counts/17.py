"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and"
when writing out numbers is in compliance with British usage.
"""

# one
# ten
# one hundred
# one hundred and fifty-five
# nine hundred and twelve
# nine hundred and ninety-nine
# one thousand


base_lookup = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

tens_lookup = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


completion_dict = {}

letter_counter = 0

for i in range (1, 1001):

    # get amt of decimals
    str_i = str(i)
    decimals = len(str_i)

    # covers 1-19
    if full := base_lookup.get(str(i)):
        completion_dict[i] = full
        continue

    if decimals == 4:
        # its 1000
        assert i == 1000 # sanity
        full = "one thousand"
        completion_dict[i] = full
        continue

    if decimals == 3:
        # must be 100-999
        hunnerds_col = base_lookup[str_i[0]]

        # check if tens col is 0 or 1
        if str_i[1] == "0":
            # 100, 200, 300
            if str_i[2] == "0":
                full = hunnerds_col + " hundred"
            # 101-109, 201-209
            else:
                full = hunnerds_col + " hundred and " + base_lookup[str_i[2]]
        
            completion_dict[i] = full
            continue

        # this will be for 10-19 sections
        if str_i[1] == "1":
            full = hunnerds_col + " hundred and " + base_lookup[str_i[1:3]]
            completion_dict[i] = full
            continue

        # must be at least 20 if we're here
            
        tens_col = tens_lookup[(str_i[1])]
        full = hunnerds_col + " hundred and " + tens_col + base_lookup[str_i[2]]
        completion_dict[i] = full
        continue

    if decimals == 2:
        # must be 20-99
        tens_col = tens_lookup[(str_i[0])]
        full = tens_col + base_lookup[str_i[1]]
        completion_dict[i] = full
        continue

for key, value in completion_dict.items():
    print(f"{key}: {value}")
    letter_counter += len(value.replace(" ", ""))

print(f"Answer is:  {letter_counter}")
# should be 21124