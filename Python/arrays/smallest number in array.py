def smallest(arr):
    min = float('inf')
    for num in arr:
        if num < min:
            min = num
    return min
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = smallest(arr)
    print(result)
if __name__ == "__main__":
    main()