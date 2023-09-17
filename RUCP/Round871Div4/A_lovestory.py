testcases = int(input())
for i in range(testcases):
    letters = input()
    sentence = "codeforces"
    count = 0
    for i in range(10):
        if letters[i] != sentence[i]:
            count+=1
    print(count)
