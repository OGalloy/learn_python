#Напишите функцию для транспонирования матрицы
from random import randint

def create_random_matrix(row: int, column: int, random_range: int):
    matrix = []
    for i in range(row):
        line = []
        for j in range(column):
            line.append(randint(0, random_range))
        matrix.append(line)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column, end = "\t")
        print()

def transpose_matrix(matrix):
    new_matrix = []
    row_number = len(matrix)
    column_number = len(matrix[0])
    new_matrix = create_random_matrix(column_number, row_number, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix




if __name__ == "__main__":
    print("Create matrix")
    new_matrix = create_random_matrix(3, 2, 10)
    print_matrix(new_matrix)
    print()
    print("Transpose matrix")
    matrixT = transpose_matrix(new_matrix)
    print_matrix(matrixT)
