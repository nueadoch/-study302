import sys
N = int(input())
arr = sorted(map(int, sys.stdin.readline().split()))

r = 1
for i in arr:
    if i == r:
        r += 1
    else:
        print(r)
        sys.exit(0)

print(arr[-1] + 1) 