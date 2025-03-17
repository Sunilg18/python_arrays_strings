n = int(input())
arr = list(map(int, input().split()))
sum = arr[0] + arr[-1]
total = arr[1] + arr[-2]
print(sum + total)