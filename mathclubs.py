def fact(n):
    """ 
	Compute the factorial of n
    >>> fact(1)
    1
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    """
    x = 1
    while n > 0:
        x = n * x
        n -= 1
    return x
   