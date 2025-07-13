n, k = map(int, input().split())
locs = []
for _ in range(n):
    locs.append(list(map(int,input().split())))
locs.sort(key = lambda x : x[0])

remneg = 0
rempos = 0
truck = 0
distance = 0
lastneg = 0
lastpos = 0

for l, num in locs:
    if l < 0:
        lastneg = min(l,lastneg)
        remneg += num
        while remneg > k:
            distance += abs(l)*2
            remneg -= min(remneg,k)
            
    if l > 0:
        lastpos = max(l,lastpos)
        rempos += num
        while rempos > k:
            distance += abs(l) * 2
            rempos -= min(rempos,k)
            
        
if remneg:
        remneg = 0
        distance += abs(lastneg)*2       
if rempos:
    rempos = 0
    distance += abs(lastpos)*2
print(distance)
            