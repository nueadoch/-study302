bar, count = 0, 1
bList= []
n = int(input())

for i in range(n) :
    bar = int(input())
    bList.append(bar)

for j in range(n-1) :
    if bList[j] > bList[n-1] :
        count += 1

print(count)