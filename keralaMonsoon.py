n = int(input())
posx = []
posy = []
for _ in range(n):
    x,y = map(int,input().split())
    posx.append(x)
    posy.append(y)
stack = []
for i in range(n):
    if not stack:
        stack.append([posx[i],posy[i]])
    elif abs(stack[-1][0]-posx[i])<=posy[i]-stack[-1][1]:
        continue
    elif abs(stack[-1][0]-posx[i])<=stack[-1][1]-posy[i]:
        stack[-1] = [posx[i],posy[i]]
    else:
        stack.append([posx[i],posy[i]])
print(len(stack))