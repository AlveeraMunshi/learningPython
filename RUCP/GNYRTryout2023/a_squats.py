def G():  # get int
    return int(input())


def GS():  # get string
    return input().strip()  # duh

n = G()
a = list(GS())
sitting = 0
for i in range(n):
    if a[i] == "x":
        sitting += 1
standing = n - sitting
less = min(sitting, standing)
operations = n//2 - less
print(operations)
index = 0
og = "X"
new = "x"
if less == standing:
    og = "x"
    new = "X"
'''while operations != 0:
    if a[index] == og:
        a[index] = new
        operations -= 1'''
for i in range(operations):
    spot = a.index(og)
    a[spot] = new
for i in range(n):
    print(a[i], end="")
