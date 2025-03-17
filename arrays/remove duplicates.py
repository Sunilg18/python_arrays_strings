n = int(input())
arr = list(map(int, input().split()))
i = 0
while(i < len(arr)):
    j = i+1
    while(j < len(arr)):
        if arr[i] == arr[j]:
            arr.pop(j)
        j += 1
    i += 1
print(*arr)