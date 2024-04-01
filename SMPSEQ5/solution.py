n = int(input())
s = input().split()
m = int(input())
q = input().split()
for i in range(min(n, m)):
  if s[i] == q[i]:
    print(i + 1, end=" ")
