testcases = int(input())
for i in range(testcases):
    length = int(input())
    array = list(map(int, input().split(" ")))
    max = 0
    blankspace = 0
    for i in range(length):
        if array[i] == 0:
            blankspace+=1
        else:
            if blankspace > max:
                max = blankspace
            blankspace = 0
    if blankspace > max:
        max = blankspace
    print(max)
