def get_number(A):
    number = 0
    
    for i in range(len(A)):
        number += A[i] * ((-2) ** i)
    
    return number

def step(X):
    m = X % -2
    
    if m < 0:
        m += 2
    
    y = (X - m) / -2
    
    return y, m

def get_negative(X):
    bits = []
    
    y = X
    
    while y != 0:
        y, m = step(y)
        bits.append(m)
    
    return bits

def solution(A):
    return get_negative(-get_number(A))