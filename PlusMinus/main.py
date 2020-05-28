def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positives += 1
        elif arr[i] < 0:
            negatives += 1
        else:
            zeros += 1
    print("{:.6f}".format(positives/len(arr)))
    print("{:.6f}".format(negatives/len(arr)))
    print("{:.6f}".format(zeros/len(arr)))

print('n = ')
n = int(input())
list = []
for i in range(0,n):
    print(str(n - i) + ' more to go')
    list.append(int(input()))
plusMinus(list)