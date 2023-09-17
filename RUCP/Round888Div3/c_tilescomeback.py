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
    
def solve():
    n, k = GM() #number of tiles in the series and length of the block
    colors = GL() #colors of the tiles
    last = colors[-1] #ends at index n
    first = colors[0] #starts at index 0
    # k of each color in the path
    # cc = defaultdict(lambda: 0) #dictionary of colors and their tile counts
    # for i in range(n): #for each tile
    #     cc[colors[i]]+=1 #add one to the count of that color
    # if (cc[first] < k or cc[last] < k): #if the first or last color has less than k tiles
    #     print("NO")
    #     return
    currcolor = first
    c = 0
    for i in range(n):
        #print(i, c, currcolor)
        if colors[i] == currcolor:
            c+=1
        if c == k and currcolor != last:
            c = 0
            currcolor = last
    if currcolor != last or c < k:
        print("NO")
    else:
        print("YES")
    
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
