#!/usr/bin/env python

import json

filename_in = 'words_dictionary.json'
filename_out = 'sorted_words.json'

with open(filename_in, 'r') as f:
	words = json.load(f)

print (len(words))

sorted_words = {}

for word in words.keys():
	sorted_word = "".join(sorted(word))
	if not sorted_word in sorted_words:
		sorted_words[sorted_word] = []
	sorted_words[sorted_word].append(word)

print(len(sorted_words))

with open(filename_out, 'w') as f:
	json.dump(sorted_words,f )

