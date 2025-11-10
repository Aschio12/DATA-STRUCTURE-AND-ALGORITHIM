t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    digits = []
    letters = []
    found_letter = False
    valid = True

    for ch in s:
        if ch.isdigit():
            if found_letter:
                valid = False  # digit comes after a letter
            digits.append(ch)
        else:  # is letter
            found_letter = True
            letters.append(ch)

    if digits != sorted(digits) or letters != sorted(letters):
        valid = False

    print("YES" if valid else "NO")
