n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
arr = arr1 + arr2
arr.sort(reverse = True)
print(*arr)