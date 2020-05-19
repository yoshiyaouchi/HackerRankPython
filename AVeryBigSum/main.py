def aVeryBigSum(ar):
    return sum(ar)

print("n =", end = " ")
list = []
for x in range(int(input())):
    print("Number " + str(x+1) + ":", end=" ")
    list.append(int(input()))

print(str(aVeryBigSum(list)))