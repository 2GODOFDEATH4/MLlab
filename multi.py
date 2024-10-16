# Example data: X (independent variables), y (dependent variable)
X = [
    [1, 2],  # First feature set
    [2, 3],  # Second feature set
    [3, 4],  # Third feature set
    [4, 5],  # Fourth feature set
    [5, 6]   # Fifth feature set
]

y = [3, 6, 7, 8, 11]  # Dependent variable (target values)

# Step 1: Add a column of 1s to X to account for the intercept term (b0)
X_b = [[1] + row for row in X]  # Each row is now [1, x1, x2]

# Step 2: Calculate X^T (transpose of X_b)
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

X_b_T = transpose(X_b)

# Step 3: Calculate X^T * X
def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):
        result_row = []
        for j in range(len(B[0])):
            sum_product = sum(A[i][k] * B[k][j] for k in range(len(B)))
            result_row.append(sum_product)
        result.append(result_row)
    return result

X_b_T_X_b = matrix_multiply(X_b_T, X_b)

# Step 4: Calculate X^T * y
X_b_T_y = matrix_multiply(X_b_T, [[yi] for yi in y])

# Step 5: Calculate the inverse of a 2x2 matrix (for simplicity)
def inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return [[d / determinant, -b / determinant],
            [-c / determinant, a / determinant]]

# Step 6: Calculate coefficients b = (X^T * X)^(-1) * (X^T * y)
X_b_T_X_b_inv = inverse_2x2(X_b_T_X_b[:2])  # Only works for 2x2
coefficients = matrix_multiply(X_b_T_X_b_inv, X_b_T_y)

# Output the intercept and coefficients
intercept = coefficients[0][0]  # b0 (intercept)
b1 = coefficients[1][0]  # b1 (coefficient for first feature)
b2 = coefficients[2][0]  # b2 (coefficient for second feature)

print(f"Intercept (b0): {intercept}")
print(f"Coefficients (b1, b2): {b1}, {b2}")

# Predict y values for the given X values using the regression line
predicted_y = [intercept + b1 * xi[0] + b2 * xi[1] for xi in X]
print(f"Predicted y-values: {predicted_y}")