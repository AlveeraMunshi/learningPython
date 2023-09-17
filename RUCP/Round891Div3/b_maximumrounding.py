from collections import defaultdict
import sys


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

def heightdiff(a, b):
    return abs(a - b)

def solve():
    xi = GS()
    x = list(map(int, xi))
    k = 1 #digit to round to
    rounding = False
    ri = len(x)
    while True:
        if rounding:
            x[len(x)-k]+=1
        if x[len(x)-k] >= 5:
            rounding = True
            ri = len(x)-k
        if x[len(x)-k] < 5:
            rounding = False
        k+=1
        if k == len(x)+1:
            break
    if x[0] >= 5:
        x.insert(0, 1)
        ri = 1
    for i in range(ri, len(x)):
        x[i] = 0
    print(''.join(map(str, x)))

            

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
