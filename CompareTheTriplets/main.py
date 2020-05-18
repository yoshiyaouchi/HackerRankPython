def compareTriplets(a, b):
    alice = 0
    bob = 0
    for x in range(3):
        if a[x] > b[x]:
            alice += 1
        elif a[x] < b[x]:
            bob += 1
        else:
            continue
    return alice, bob

alice = []
bob = []

for x in range(3):
    print("Rate Alice #" + str(x+1) + ":")
    alice.append(int(input()))

for x in range(3):
    print("Rate Bob #" + str(x+1) + ":")
    bob.append(int(input()))

result = compareTriplets(alice, bob)
print(result)