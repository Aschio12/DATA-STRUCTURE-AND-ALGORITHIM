for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    i = 0
    while i < n:
        if arr[i] != 0:
            i += 1
            continue
        j = i
        while j < n and j - i < k and arr[j] == 0:
            j += 1
        if j - i == k:
            count += 1
            i = j + 1
        else:
            i = j + 1
    print(count)