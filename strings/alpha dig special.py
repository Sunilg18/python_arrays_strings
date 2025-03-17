import sys
def count(str):
    digits = 0
    alpha = 0
    sp = 0
    for i in str:
        if i.isdigit():
            digits += 1
        elif i.isalpha():
            alpha += 1
        else:
            sp += 1
    print(digits)
    print(alpha)
    print(sp)
if __name__ == "__main__":
    str = input().strip()
    count(str)