# test

from math import sqrt
t = int(input())
for i in range(t):
  a, b, c, z, y, x = map(int, input().split())
  X = b * b + c * c - x * x
  Y = a * a + c * c - y * y
  Z = a * a + b * b - z * z
  vol = sqrt(4 * a * a * b * b * c * c - a * a * X * X - b * b * Y * Y - c * c * Z * Z + X * Y * Z) / 12
  print(round(vol, 4))
