"""
@author: Anirudh Sharma
"""


def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        print("Bubble Sort: ", L)
        for i in range(1, len(L)):
            if L[i - 1] > L[i]:
                temp = L[i - 1]
                L[i - 1] = L[i]
                L[i] = temp
                swap = False

test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(test)