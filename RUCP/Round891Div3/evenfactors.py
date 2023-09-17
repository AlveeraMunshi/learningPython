n = int(input())
exist = False
'''
for a in range(2,int(n/2)+1):
    if n%a == 0:
        b=n/a
        if (a+b)%2 == 0:
            print(a,b)
            exist = True
            break
'''
#false for all primes
#true for evens if n/2 is even
#true for odds if two odd factors exist
if n%2 == 0:
    b=n/2
    if b%2 == 0:
        print(a,b)
        exist = True
else:
    exist = True

print("YES" if exist else "NO")