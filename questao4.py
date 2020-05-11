def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
    We're assuming here that the_board is a permutation of column
    numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def solve_queens(n):
    import random
    import time

    t = 0
    rng = random.Random()   # Instantiate a generator
    print(n)
    bd = list(range(n))     # Generate the initial permutation
    tries = 0
    t1 = time.time()
    delta = 0
    while tries < 10 and delta < 60:
       rng.shuffle(bd)
       if not has_clashes(bd):
           t2 = time.time()
           delta = t2 - t1
           print("Found solution {0} in {1} seconds.".format(bd,delta))
           tries +=1
           t += t2-t1
           t1 = t2
    if tries == 11:
        print('mean time: {}'.format(t/10))


def solve_queens_1min():
    import random
    import time
    t = 0
    rng = random.Random()   # Instantiate a generator
    n = 12
    bd = list(range(n))     # Generate the initial permutation
    delta = 0
    t1 = time.time()
    while delta < 60:
       rng.shuffle(bd)
       if not has_clashes(bd):
           print("".format(n))
           t2 = time.time()
           delta = t2 - t1
           n = n+1
           bd = list(range(n)) 
           t1 = time.time()
    print('The maximum size puzzle we can usually solve in under a minute is: {}'.format(n-2))


solve_queens_1min()
solve_queens(4)
solve_queens(12)
solve_queens(16)
