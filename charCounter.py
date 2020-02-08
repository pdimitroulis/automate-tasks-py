#Goal: print a dic which includes how many times appeared every letter in the given string

from pprint import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'   # //PARAMETER//
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint(count)
