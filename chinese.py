n = int(input())
day = list(map(int,input().split()))
night = list(map(int,input().split()))
x = int(input())
overtime = 0
day.sort()
night.sort(reverse = True)
for i in range(n):
    if (day[i] + night[i]) > x:
        overtime += ((day[i] + night[i]) - x)
print(overtime * 100 if overtime > 0 else 0)