import random

randomList = []
for f in range(0, 1000000):
    n = random.randint(0, 1000000000)
    randomList.append(n)

with open('random.csv', 'w') as f:
    for item in randomList:
        f.write("%s\n" % item)
randomList.sort()
with open('sorted.csv', 'w') as f:
    for item in randomList:
        f.write("%s\n" % item)
randomList.sort(reverse=True)
with open('reverse.csv', 'w') as f:
    for item in randomList:
        f.write("%s\n" % item)