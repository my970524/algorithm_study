i, j = map(int, input().split())

boong = [input() for _ in range(i)]

for b in boong:
  b = b[::-1]
  print(b)
  