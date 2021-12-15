with open('input.txt', 'r') as f:
    file = [int(line) for line in f.readlines()]

#for each item, check if it is greater than the previous item
#if it is, increment numIncrements
numIncrements = 0
for i, j in enumerate(file):
    if j > file[i-1]:
        numIncrements += 1
print(numIncrements)