# Example data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Calculate the means of x and y
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Calculate the terms needed for the slope (b1) and intercept (b0)
n = len(x)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x = sum(x)
sum_y = sum(y)
sum_x_squared = sum(xi ** 2 for xi in x)

# Calculate slope (b1) and intercept (b0)
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b0 = (sum_y - b1 * sum_x) / n

# Print the coefficients
print(f"Intercept (b0): {b0}")
print(f"Slope (b1): {b1}")

# Predict y values for the given x values using the regression line
predicted_y = [b0 + b1 * xi for xi in x]
print(f"Predicted y-values: {predicted_y}")