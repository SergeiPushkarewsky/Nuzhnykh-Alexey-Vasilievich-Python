def func(matrix):
    ans = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if (matrix[i][j] == matrix[i][j + 1] and
                matrix[i][j] == matrix[i + 1][j] and
                matrix[i][j] == matrix[i + 1][j + 1]):
                ans.append("R: " + str(i) + ", C: " + str(j))
    return ans;
n, m = map(int, input("Введите NxM: ").split())
matrix = [[0] * m] * n
print("Заполните матрицу: ")
for i in range(len(matrix)):
    matrix[i] = input().split()
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])
ans = func(matrix)
print(ans)