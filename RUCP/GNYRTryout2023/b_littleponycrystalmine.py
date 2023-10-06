def G():  # get int
    return int(input())

n = G()
a = []
for i in range(1,n+1,2):
    ds = str("*"*((n-i)//2) + "D"*(i) + "*"*((n-i)//2))
    a.append(ds)
for i in range(len(a)-2,-1,-1):
    a.append(a[i])
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="")
    print()
        
