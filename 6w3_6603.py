from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]

    s = list(combinations(s, 6))
    for i in s:      # 각 그룹에서
        for j in i:  # 하나씩 뽑아서
            print(j, end=' ')
        print()
    print()