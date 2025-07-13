n, a, b = map(int,input().split())
buildings = []
dis = []
for i in range(n):
    x,y = map(int,input().split())
    dis.append([abs(a-x)+abs(b-y), i+1])

dis.sort(key = lambda x: x[0])

for i in range(len(dis)):
    print(dis[i][1], end= ' ')
print()