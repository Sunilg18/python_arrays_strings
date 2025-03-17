def second_max(arr):
    first = second = float('-inf')
    for i in arr:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    return second
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = second_max(arr)
    print(result)
if __name__ == "__main__":
    main()