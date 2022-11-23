import csv
import re
import numpy as np

res1 = []
res2 = []

file_name = input()

with open(file_name, encoding="utf-8-sig") as f:
    file_result = csv.reader(f)
    for line in file_result:
        res1.append(line)

name = res1.pop(0)

for line in res1:
    if len(name) == len(line) and '' not in line:
        for i in line:
            i = re.sub(r'<[^<>]*>', '', i)
            i = re.sub(r'\n', ', ', i)
            i = str.strip(re.sub(r'\s+', ' ', i))
            res2.append(i)

res3 = []

if len(res2) > 0:
    splits = np.array_split(res2, len(res2) / len(name))
    for array in splits:
        res3.append(array)
    for k in range(0, len(res3)):
        for i in range(0, len(name)):
            print(name[i] + ': ' + res3[k][i])
        print()