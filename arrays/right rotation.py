def reverse(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    pos = int(input())
    pos = pos%n
    reverse(arr, 0, n-1)
    reverse(arr, 0, pos-1)
    reverse(arr, pos, n-1)
    for i in arr:
        print(i, end=' ')
if __name__ == "__main__":
    main()
