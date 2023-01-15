import numpy as np # for matrix vector generation

# intialize random matrix and vector of integers
vector = np.random.randint(10, size=(4))
matrix = np.random.randint(10, size=(4, 4))

# Intialize matrix vector
v = [1, 4, 5, 6]
m = [
    [5, 6, 3, 10],
    [10, 4, 1, 2],
    [0, 5, 2, 27],
    [4, 55, 9, 1]
]

# To perfrom sequential matrix vector multiplication
def sequential_multiplication(m, v):
    """to perfom sequential multiplication
    time O(n2)
    INPUT
    -----
    m: matrix
    v: vector
    OUTPUT
    ------
    result: result vector
    """
    results = [0 for i in range(len(m))]
    for i in range(len(m)):
        r = 0
        for j in range(len(v)):
            r += m[i][j] * v[j]
        results[i] = r
    return results

# Print the result
print(sequential_multiplication(m, v))