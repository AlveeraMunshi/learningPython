'''
6
4
2 00
3 10
4 01
4 00
5
3 01
3 01
5 01
2 10
9 10
1
5 11
3
9 11
8 01
7 10
6
4 01
6 01
7 01
8 00
9 01
1 00
4
8 00
9 10
9 11
8 11
'''

testcases = int(input())
for i in range(testcases):
    bookn = int(input())
    totaltime = 10**6
    skill1book = 10**6
    skill2book = 10**6
    for i in range(bookn):
        book = input().split(" ")
        minutes = int(book[0])
        if book[1] == "11":
            totaltime = min(minutes, totaltime)
        elif not book[1] == "00":
            if book[1][0] == "1":
                skill1book = min(minutes, skill1book)
            if book[1][1] == "1":
                skill2book = min(minutes, skill2book)
    totaltime = min(totaltime, skill1book + skill2book)
    if totaltime >= 10**6:
        totaltime = -1
    print(totaltime)