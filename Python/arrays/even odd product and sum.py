n = int(input())
arr = list(map(int, input().split()))
even = 1
odd = 0
for i in arr:
    if i%2==0:
        even *= i
    else:
        odd += i
print(even)
print(odd)