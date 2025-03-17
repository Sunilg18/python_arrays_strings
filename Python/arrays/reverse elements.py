def reverse(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    reverse(arr, 0, n-1)
    for i in arr:
        print(i, end=' ')
if __name__ == "__main__":
    main()
        