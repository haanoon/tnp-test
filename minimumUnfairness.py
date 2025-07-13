l = list(map(int, input().split(',')))
k = int(input())
l.sort()
start = 0
i = 0
m = float('inf')

for i in range(k-1,len(l)):
    a = l[i-k+1:i+1]
    mini = max(a) - min(a)
    if mini < m:
        start = i
        m = mini
    
for i in l[start-k+1:start+1]:
    print(i, end=' ')
print()
