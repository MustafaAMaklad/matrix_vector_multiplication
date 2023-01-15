# import required modules
import concurrent.futures
import time
import numpy as np


# intialize random matrix and vector of integers
array = np.random.randint(10, size=(4))
mat = np.random.randint(10, size=(4, 4))

# intialize matrix and vector
v = [1, 4, 5, 6]
m = [
    [5, 6, 3, 10],
    [10, 4, 1, 2],
    [0, 5, 2, 27],
    [4, 55, 9, 1]
]

# To perfom dot product between two vectors
# which will be the task to be given for each thread
def dot_product(m, v):
    """ performs dot product of two vectors and returns result
    """
    t = 0
    for i in range(len(v)):
        t += m[i] * v[i]
    return t

def parallel_multiplication(m, v):
    """to performs parallel multiplication and returns result
    time O(n)
    speed up = n
    cost = n2
    eff = 1
    INPUT
    -----
    m: matrix
    v: vector
    OUTPUT
    ------
    result: result vector
    """
    # context manager to use threadpool
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # start counting time
        start = time.perf_counter()

        # creat threads and give them dot product task concurrently
        results = [executor.submit(dot_product, m[i], v).result() for i in range(len(m))]

        # end counting time 
        end = time.perf_counter()

    # print time taken by the algorithm
        print(f"Elapsed {round((end - start) * 10 ** 6, 2)} micro sec(s).")

    return results

# print result

print(parallel_multiplication(m, v))


