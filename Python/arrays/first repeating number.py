n = int(input())
arr = list(map(int, input().split()))
seen = set()
for i in arr:
    if i in seen:
        print(i)
        exit()
    seen.add(i)