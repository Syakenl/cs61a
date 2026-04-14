def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        for i in range(1,n+1):
            if cond(i):
                print(i)
    return f

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if (x % 10) != ((x//(10 ** k))%10):
                return False
            x //= 10
        return True
    return check


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return- 1
    else:
        return 0

def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.

    >>> ramp(123)   # 2 increases (1-> 2, 2-> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1-> 3, 1-> 5) and 1 decrease (3-> 1)
    True
    >>> ramp(176)   # 1 increase (1-> 7) and 1 decrease (7-> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    n, last, tally =n//10, n%10 , 0

    while n:
        n, last, tally = n // 10, n % 10, tally + sign(last -(n%10))
    return tally>0

def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT.
    """ 

    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()

def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.

    >>> f, g = ups(3)
    >>> process(1200849, f, g)    # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)      # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)  # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)          # 0 increases
    False
    """
    def f(left, right):
        res = k - max(0,sign(right-left))
        return ups(res)
    return f, lambda: k == 0



def only(n, t):
    """Return only the digits of n for which t returns True when called on each digit

    >>> only(23344567, lambda d: d % 2 == 0)
    2446
    >>> only(987654349675, lambda d: d < 7)
    6543465
    >>> only(2023, lambda d: False)
    0
    """
    keep = 0
    while n:
        n, d = n // 10, n % 10
        if t(d):
            keep = 10 * keep + d
    while keep:
        n, keep =10*n+keep%10 , keep // 10
    return n


def every(t):
    """Return a function that returns whether t is True 
    for every digit of non-negative n.

    >>> f = every(lambda d: d % 2 == 1)
    >>> f(37511)  # every digit is odd
    True
    >>> f(2023)   # Not every digit is odd
    False
    """
    def digit(n):
        while n:
            if not t(n%10):
                return False
            n = n // 10
        return True
    return digit

