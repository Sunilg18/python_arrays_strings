def seperate(arr):
    even = []
    odd = []
    for num in arr:
        if num %2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.sort()
    odd.sort()
    return even + odd
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = seperate(arr)
    print(*result)
if __name__ == "__main__":
    main()
