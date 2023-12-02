import re

digits = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(in_val):
    for k, v in digits.items():
        in_val = in_val.replace(k, v)
    return in_val

def set_cal(in_val):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", in_val).split("\n"))

in_val = open("part_b.txt").read()
print(set_cal(replace_words(in_val)))