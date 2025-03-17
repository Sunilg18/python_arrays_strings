n = int(input())
arr = list(map(int, input().split()))
seen = set()
last = -1
for i in arr:
    if i in seen:
        last = i
    seen.add(i)
if(last != -1):
    print(last)
else:
    print("no")