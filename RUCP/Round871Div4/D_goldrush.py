testcases = int(input())
for i in range(testcases):
    pilesizes = input().split()
    n = int(pilesizes[0])
    m = int(pilesizes[1])
    piles = []
    piles.append(n)
    # pile 1 is i and pile 2 is 2i, i + 2i = n, 3i = n, i = n/3
    possible = False
    i = 0
    while (i < len(piles) and m < n):
        while (piles[i] % 3 == 0):
            piles.append(piles[i]/3*2)
            piles.append(piles[i]/3)
            piles.remove(piles[i])
            if (piles[i] == m):
                possible = True
                break
        i+=1
    if possible:
        print("YES")
    else:
        print("NO")