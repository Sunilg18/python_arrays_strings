def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return "Not balanced"
    
    return "Balanced" if not stack else "Not balanced"

if __name__ == "__main__":
    s = input().strip()
    print(is_balanced(s))