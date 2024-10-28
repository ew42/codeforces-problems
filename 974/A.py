t = int(input())

for tests in range(t):
    n, k = map(int, input().split())

    lyst = [int(x) for x in input().split()]

    gold = 0
    count = 0
    for a in lyst:
        if a >= k:
            gold += a
        elif a == 0:
            if gold > 0:
                count += 1
                gold -= 1
    print(count)
