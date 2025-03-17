n = int(input())
arr = list(map(int, input().split()))
arr[0], arr[1], arr[-1], arr[-2] = arr[-2], arr[-1], arr[1], arr[0]
print(*arr)