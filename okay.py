#!/usr/bin/env python
import sys
import json
import itertools

filename = 'sorted_words.json'

with open(filename, 'r') as f:
	anagrams = json.load(f)


def check(word):
	letters = "".join(sorted(word))
	try:
		return anagrams[letters]
	except KeyError:
		return []
word = "".join(sorted(sys.argv[1]))


words = set()
for r in reversed(range(5, len(word)+1)):
	for combination in itertools.combinations(word, r):
		for x in check(combination):
			words.add(x)

words = sorted(sorted(list(words)), key=len)
print("\n".join(words))
