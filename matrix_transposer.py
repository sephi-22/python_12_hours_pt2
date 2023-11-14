#Write a function that transposes a matrix represented as a list of lists.
#Hint: Nested list comprehensions can be used to invert rows and columns
#Transpose is swapping lists and columns

def transpose_matrix(matrix):
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed_matrix

matrix_1 = [
    [1,2,3,4],
    [4,5,6,5],
    [7,8,9,10]
]

print(transpose_matrix(matrix_1))