t = int(input())
for tests in range(t):
    n, k = map(int, input().split())
    leaves = 0
    for year in range(n-k+1, n+1):
        if year % 2 != 0:
            leaves += 1
    if leaves % 2 == 0:
        print("YES")
    else: 
        print("NO")
