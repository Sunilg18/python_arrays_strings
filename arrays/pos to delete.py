n = int(input())
arr = list(map(int, input().split()))
pos = int(input())
for i in range(pos, n-1):
    arr[i] = arr[i+1]
arr = arr[:-1]
print(*arr)