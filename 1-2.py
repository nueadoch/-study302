oldList, newList, tList = [], [], []
tmp = 0
n = int(input())

for i in range(n, 0, -1) :
    oldList.append(i)

print(oldList)

while(len(oldList) > 1) :
    newList.append(oldList.pop())

    tList.append(oldList.pop())
    for j in range(len(oldList)) :
        tList.append(oldList[j])
    oldList.clear()
    for k in range(len(tList)) :
        oldList.append(tList[k])
    tList.clear()


print(newList)
print(oldList)