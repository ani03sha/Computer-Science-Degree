"""
@author: Anirudh Sharma
"""


def selection_sort(L):
    suffix_start = 0
    while suffix_start != len(L):
        print("Selection Sort:", L)
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                L[suffix_start], L[i] = L[i], L[suffix_start]
        suffix_start += 1
        
test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(test)