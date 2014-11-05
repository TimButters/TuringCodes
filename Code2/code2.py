#!/usr/bin/python

INFILE = open("C2")
LINES = INFILE.readlines()

chars = []
for line in LINES:
    chars.append(line.split())

flat_chars = [c for each in chars for c in each]

counts = {}
for c in flat_chars:
    if c in counts.keys():
        counts[c] += 1
    else:
        counts[c] = 1

print(sorted(counts, key=counts.get, reverse=True))

letters = []
freq = []
for k, v in counts.items():
    letters.append(k)
    freq.append(v)
index = list(range(0, len(letters)))

import matplotlib.pyplot as plt
import numpy as np

freq = np.array(freq)
rel_freq = freq / freq.sum()
inds = rel_freq.argsort()
rel_freq = rel_freq[inds[::-1]]
letters = np.array(letters)
letters = letters[inds[::-1]]

bar_width = 0.5
plt.bar(index, rel_freq, bar_width)
plt.xticks(np.array(index) + bar_width, letters)

plt.show()
