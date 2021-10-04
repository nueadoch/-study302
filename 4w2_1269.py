A, B = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

union = len(set(arrA + arrB))
dif = len(arrA+arrB) - union

print(union - dif)