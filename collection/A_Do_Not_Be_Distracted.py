for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    seen = [False] * 26
    i = 0
    valid = True
    while i < n:
        char = s[i]
        idx = ord(char) - ord('A')
        if seen[idx]:
            valid = False
            break
        j = i
        while j < n and s[j] == char:
            j += 1
        seen[idx] = True
        i = j
    print("YES" if valid else "NO")