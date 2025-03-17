n = int(input())
arr = list(map(int, input().split()))
count = 0
arr.sort()
length = len(arr)
maj = arr[n // 2]
for i in arr:
    if i == maj:
        count += 1
if count > length // 2:
    print(maj)
else:
    print("no")