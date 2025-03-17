n = int(input())
arr = list(map(int, input().split()))
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
for key, value in freq.items():
    print(f"{key} occurs {value} times")