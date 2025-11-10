for _ in range(int(input())):
    n = int(input())
    max_quality = float("-inf")
    winner_index = -1
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10:
            if b > max_quality:
                max_quality = b
                winner_index = i + 1
    print(winner_index)