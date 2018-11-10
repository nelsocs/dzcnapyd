import os
filepath = '/home/chrisnelson/move/CL-logs/all-uniq-src.accept'
fo = open(filepath, 'r')
line = fo.read(-1)
print(line)
fo.close
