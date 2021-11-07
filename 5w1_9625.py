n = int(input())
a = [1]
b = [0]

for i in range(n):
  a.append(b[i])
  b.append(a[i] + b[i])

print(a[-1], b[-1])