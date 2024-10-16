# Sample data
x = [1, 2, 3, 4, 5]  # Independent variable
y = [2, 8, 18, 32, 50]  # Dependent variable

# Step 1: Transform the input data for polynomial regression
def create_polynomial_features(x, degree):
    return [[x_i ** d for d in range(degree + 1)] for x_i in x]

degree = 2  # Degree of the polynomial
X_poly = create_polynomial_features(x, degree)

# Step 2: Calculate the transpose of X_poly
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

X_poly_T = transpose(X_poly)

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

X_poly_T_X_poly = matrix_multiply(X_poly_T, X_poly)

# Step 4: Calculate X^T * y
y_matrix = [[yi] for yi in y]  # Convert y to a column vector
X_poly_T_y = matrix_multiply(X_poly_T, y_matrix)

# Step 5: Calculate the inverse of a matrix (using Gaussian elimination)
def inverse(matrix):
    n = len(matrix)
    # Create an augmented matrix with the identity matrix
    augmented = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform Gaussian elimination
    for i in range(n):
        # Make the diagonal contain all 1's
        diag = augmented[i][i]
        for j in range(len(augmented[i])):
            augmented[i][j] /= diag
        for j in range(n):
            if j != i:
                factor = augmented[j][i]
                for k in range(len(augmented[j])):
                    augmented[j][k] -= factor * augmented[i][k]

    # Extract the right half of the augmented matrix which is the inverse
    return [row[n:] for row in augmented]

# Step 6: Calculate coefficients b = (X^T * X)^(-1) * (X^T * y)
X_poly_T_X_poly_inv = inverse(X_poly_T_X_poly)
coefficients = matrix_multiply(X_poly_T_X_poly_inv, X_poly_T_y)

# Output the coefficients
print("Coefficients (b0, b1, b2):", [c[0] for c in coefficients])

# Predict y values using the polynomial regression model
predicted_y = [sum(coefficients[j][0] * (x_i ** j) for j in range(degree + 1)) for x_i in x]
print("Predicted y-values:", predicted_y)