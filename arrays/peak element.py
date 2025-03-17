n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if(i == 0 and arr[i] > arr[i+1]):
        print(arr[i])
    elif(i == n-1 and arr[i] > arr[i-1]):
        print(arr[i])
    elif(i > 0 and i < n-1 and arr[i] > arr[i+1] and arr[i] > arr[i-1]):
        print(arr[i])