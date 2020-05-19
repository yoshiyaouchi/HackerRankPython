def diagonalDifference(arr):
    length = len(arr)
    leftToRight = 0
    rightToLeft = 0
    for i in range(length):
        leftToRight += arr[i][i]
        rightToLeft += arr[i][length-i-1]
    return abs(leftToRight-rightToLeft)

arr = []
print("n =", end = " ")
n = int(input())
matrix = n * n

for i in range(n):
    column = []
    for j in range(n):
        print(str(matrix) + " to go!: ", end = "")
        column.append(int(input()))
        matrix -= 1
    arr.append(column)

print("The absolute difference between the sums of the matrix's two diagonals is: " + str(diagonalDifference(arr)))