#!/bin/python3


def checkRansom(magazine, note):
    dict = {}
    for word in magazine:
        dict[word] = dict.get(word, 0) + 1
    for word in note:
        if dict.get(word, 0) == 0:
            print('False')
            return
        else:
            dict[word] -= 1
    print('True')


if __name__ == '__main__':
    Na = int(input())

    A = ""
    for i in range(Na):
        A += input()

    Nb = int(input())

    B = ""
    for i in range(Nb):
        B += input()

    checkRansom(B, A)
