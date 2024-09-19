i = int(input(""))
for iterations in range(i):
    alice = [int(x) for x in input("") if x.isdigit()]
    bob = [int(x) for x in input("") if x.isdigit()]
    alice = [x for x in range(alice[0], alice[1] + 1)]
    bob = [x for x in range(bob[0], bob[1] + 1)]
    count = 1
    for x in alice:
        if x in bob:
            count += 1
    print(count)
