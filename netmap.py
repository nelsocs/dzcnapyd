import os
filepath = '/home/%user/%filename'
fo = open(filepath, 'r')
line = fo.read(-1)
print(line)
fo.close

# this file works with networkmap.py and nutrients.py to pull edges from currated logs
