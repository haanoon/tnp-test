n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))
v1.sort()
v2.sort(reverse = True)
s = 0
for i in range(n):
    s += (v1[i]*v2[i])
print(s)