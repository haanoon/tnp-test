n = int(input())
locs = []
xt = 0
yt = 0
for i in range(n):
    x, y = map(int, input().split())
    xt += x
    yt += y
print(xt//n, yt//n)
