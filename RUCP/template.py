def G():  # get int
    return int(input())


def GS():  # get string
    return input().strip()  # duh


def GM():  # get multiple ints
    return map(int, input().split())


def GL():  # get list of ints
    return list(map(int, input().split()))
