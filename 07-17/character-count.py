import pprint

message = 'All cows eat grass'

count = {}

for character in message:
    count.setdefault(character.lower(), 0)
    count[character.lower()] += 1

pprint.pprint(count)