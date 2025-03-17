n = int(input())
arr = list(map(int, input().split()))
pos = int(input())
for i in range(0, pos):
    last = arr[0]
    for j in range(0, n-1):
        arr[j] = arr[j+1]
    arr[-1] = last
print(*arr)