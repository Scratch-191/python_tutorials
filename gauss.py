import numpy as np

def gauss_seidel(A, b, initial_guess, num_iterations):
    n = len(b)
    x = initial_guess.copy()
    
    for k in range(num_iterations):
        x_new = np.zeros(n)
        
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        
        error = np.linalg.norm(x_new - x)
        print(f"Iteration {k + 1}: x = {x_new}, Error = {error}")
        
        x = x_new.copy()
    
    return x

# Example system of equations: Ax = b
A = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]])

b = np.array([7, -8, 6])

# Initial guess
initial_guess = np.array([0, 0, 0])

# Number of iterations
num_iterations = 4

# Solve using Gauss-Seidel method
solution = gauss_seidel(A, b, initial_guess, num_iterations)
print("\nSolution:", solution)
