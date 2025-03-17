def repeated(arr):
    element = {}
    for num in arr:
        element[num] = element.get(num, 0)+1
    total = 0
    for num, count in element.items():
        if count == 1:
            total += num
    return total
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = repeated(arr)
    print(result)
if __name__ == "__main__":
    main()