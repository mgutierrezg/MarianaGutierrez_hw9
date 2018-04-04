import numpy as np

def fibonacci(N):
    if (N == 0 or N == 1):
        return N
    else:
        return fibonacci(N-1) + fibonacci(N-2)

def get_time(N):
    import time
    t0 = time.time()
    fibonacci(N)
    t1 = time.time()-t0
    return t1

N = 0;
while(N <= 35):
    print N,",",get_time(N)
    N += 1
