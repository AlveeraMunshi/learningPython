from collections import defaultdict
import sys

if "pypy" in sys.argv[0]:
    import io
    import os

    readline = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    def input():
        return readline().decode()

    def print(*x, end="\n") -> None:
        sys.stdout.write(" ".join(map(str, x)) + end)

else:
    _print = print

    def print(*x, **kwargs) -> None:  # type: ignore
        _print(f"\033[38;2;20;255;20m{' '.join(map(str, x))}\033[0m", **kwargs)


def range2(n, m):
    for i in range(n):
        for j in range(m):
            yield i, j


def G():  # get int
    return int(input())


def GS():  # get string
    return input()  # duh


def GM():  # get multiple ints
    return map(int, input().split())


def GL():  # get list of ints
    return list(map(int, input().split()))


def grid_neighbor(i, j):
    return ((i + 1), j), ((i - 1), j), (i, (j + 1)), (i, (j - 1))


def grid_bfs():
    seen = [[False] * m for _ in range(n)]

    for i, j in range2(n, m):
        if not g[i][j] or seen[i][j]:
            continue
        # component logic starts here
        seen[i][j] = True
        q = [(i, j)]

        while q:
            i, j = q.pop()
            # every cell in component processed here
            for ni, nj in grid_neighbor(i, j):
                if 0 <= ni < n and 0 <= nj < m and g[ni][nj] and not seen[ni][nj]:
                    seen[ni][nj] = True
                    q.append((ni, nj))
        # after bfs logic


MULT = 1

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

'''
def sortable(a, n, v):
    first = a[v]
    smallestswap = v
    for i in range(n): # go through entire list
        if first > a[i] and first%2 == a[i]%2 and a[i] < a[smallestswap]: # if curr val is larger, same parity, and smaller than smallestswap
            smallestswap = i
    swap(a, v, smallestswap) # swap smallestswap with v
    for i in range(n):
        if a[i] > a[i-1]: # if a[i] is larger than a[i-1], then it is not sorted
            if i == v:
                return False
            return sortable(a, n, i)
    return True
'''
#attempt 2
'''
def sorted(a, n):
    #check if sorted
    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True

def sortable(a, n, v):
    #print(a)
    if sorted(a, n): # if sorted, then return true
        return True
    if v >= n: # if v is n, then we have gone through the entire list
        return sorted(a, n) # check if sorted
    curr = a[v] # curr is the current value
    smallestswap = v # smallestswap is the index of the smallest value that is larger than curr
    for i in range(v+1, n): # go through remainder of list
        if curr > a[i] and curr%2 == a[i]%2 and a[i] < a[smallestswap]: # if curr val is larger, same parity, and smaller than smallestswap
            smallestswap = i
    swap(a, v, smallestswap) # swap smallestswap with v
    return sortable(a, n, v+1) # call sortable with v+1
'''

def sortable(a, n):
    b = sorted(a)
    for i in range(n):
        if a[i]%2 != b[i]%2:
            return False
    return True
    
def solve():
    n = G() # length of array a
    a = GL() # array a
    if sortable(a, n):
        print("YES")
    else:
        print("NO")
    
    #import time
    #time.sleep(0.1)
        



for _ in range(G() if MULT else 1):
    try:
        solve()
    except Exception as e:
        import threading
        import time

        threading.Thread(
            target=lambda: [input() for _ in range(10**100)], daemon=True
        ).start()
        time.sleep(0.1)
        raise e
