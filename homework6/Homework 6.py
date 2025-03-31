import numpy as np

#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    return arr[np.any(np.vectorize(is_prime)(arr), axis=1)]
arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsPrimes(arr))

#2.1
def checkerboard():
    return np.zeros((8, 8), int)
print(checkerboard())

#2.2
def checkerboard():
    board = np.zeros((8, 8), int)  
    board[::2, ::2] = 1  
    return board
print(checkerboard())

#2.3
def checkerboard():
    board = np.zeros((8, 8), int)  
    board[::2, ::2] = 1  
    board[1::2, 1::2] = 1  
    return board
print(checkerboard())

#2.4
def reverse_checkerboard():
    board = np.ones((8, 8), int)  
    board[::2, ::2] = 0  
    board[1::2, 1::2] = 0  
    return board
print(reverse_checkerboard())

#3
def expansion(strings, spaces):
    return np.array([" ".join(list(word)).replace(" ", " " * spaces) for word in strings])
universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))  
print(expansion(universe, 2))  

#4
def secondDimmest(stars):
    return np.sort(stars, axis=0)[1] 
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(secondDimmest(stars))