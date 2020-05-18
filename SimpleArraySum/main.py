# Method 1
def simpleArraySum(ar):
    "Sums the array of integers"
    return sum(ar)

# Method 2
def simpleArraySum2(ar):
    length = len(ar)
    sum = 0
    for x in range(length):
        sum += ar[x]
    return sum

n = int(input())
list = []
for x in range(n):
    list.append(int(input()))

result = simpleArraySum2(list)
print(str(result))