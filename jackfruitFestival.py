n, day = map(int,input().split())
jacks = list(map(int,input().split()))
jacks.sort(reverse = True)
print(sum(jacks[:day]))