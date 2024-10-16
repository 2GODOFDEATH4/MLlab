import math

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Predict function (hypothesis)
def predict(features, weights):
    z = sum([w * x for w, x in zip(weights, features)])
    return sigmoid(z)

# Cost function (Binary Cross Entropy Loss)
def cost_function(X, y, weights):
    m = len(y)
    total_cost = 0
    for i in range(m):
        prediction = predict(X[i], weights)
        total_cost += -y[i] * math.log(prediction) - (1 - y[i]) * math.log(1 - prediction)
    return total_cost / m

# Gradient Descent
def update_weights(X, y, weights, alpha):
    m = len(y)
    gradients = [0] * len(weights)
    for i in range(m):
        prediction = predict(X[i], weights)
        for j in range(len(weights)):
            gradients[j] += (prediction - y[i]) * X[i][j]
    
    # Update each weight
    for j in range(len(weights)):
        weights[j] -= alpha * gradients[j] / m

    return weights

# Logistic regression function
def logistic_regression(X, y, alpha, iterations):
    weights = [0.0] * len(X[0])
    
    for i in range(iterations):
        weights = update_weights(X, y, weights, alpha)
        if i % 100 == 0:  # Print cost every 100 iterations
            cost = cost_function(X, y, weights)
            print(f'Iteration {i}: Cost {cost}')

    return weights

# Example dataset (with intercept term)
X = [[1, 2.0], [1, 3.0], [1, 4.0], [1, 5.0]]  # 1 for bias term
y = [0, 0, 1, 1]

# Hyperparameters
alpha = 0.1  # Learning rate
iterations = 1000  # Number of iterations

# Train the model
weights = logistic_regression(X, y, alpha, iterations)

# Output the final weights
print(f'Final weights: {weights}')

# Predict the probability of a new example
new_example = [1, 3.5]  # Include the bias term
prediction = predict(new_example, weights)
print(f'Prediction for {new_example}: {prediction}')
