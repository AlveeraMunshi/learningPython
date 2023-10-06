from collections import defaultdict


def G():  # get int
    return int(input())

def GM():  # get multiple ints
    return map(int, input().split())

def GL():  # get list of ints
    return list(map(int, input().split()))

n = G()
a = GL()
a.sort()
boxes = []
for i in range(n-2):
    if a[i] < a[i+1]:
        a.pop(i)
print(len(a)-1)

#print(candies[0][0])



