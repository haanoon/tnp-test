n = int(input())
posx = []
posy = []
for _ in range(n):
    x,y = map(int,input().split())
    posx.append(x)
    posy.append(y)
stack = []

# for i in range(n):
#     x,y = posx[i], posy[i]
#     if len(stack) > 1:
#         for j in range(len(stack) - 1):
#             sx, sy = stack[j]
#             if abs(sx - x) <= (sy - y):
#                 stack.pop(j)
#     if stack:
#         if abs(stack[-1][0] - x) > (y - stack[-1][0]):
#             stack.append([x,y])
#     else:
#         stack.append([x,y])
# if len(stack)>1:
#     for j in range(len(stack) - 1):
#         if abs(stack[j][0]-stack[-1][0]) <= (stack[-1][1] - stack[j][1]):
#             stack.pop(j)
            
# print( len(stack))


for i in range(n):
    if len(stack)>1:
        for j in range(len(stack) - 1):
            if abs(stack[-1][0] - stack[j][0]) <= (stack[-1][1]-stack[j][0]):
                stack.pop(j)

    if stack:
        if abs(stack[-1][0]-posx[i]) > (posy[i] - stack[-1][1]):
            stack.append([posx[i],posy[i]])
    else:
        stack.append([posx[i],posy[i]])
if len(stack)>1:
    for j in range(len(stack) - 1):
        if abs(stack[-1][0] - stack[j][0]) <= (stack[-1][1]-stack[j][0]):
            stack.pop(j) 
print( len(stack))