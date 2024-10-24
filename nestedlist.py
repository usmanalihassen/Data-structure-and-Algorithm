# A 2D matrix (3 rows and 3 columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the nested list
print(matrix[0])      
print(matrix[1][2])  

# Looping through each row
for row in matrix:
    print(row)

# Flattening the matrix into a single list (nested list comprehension)
flat_matrix = [item for row in matrix for item in row]
print(flat_matrix)    
