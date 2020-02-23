"""
@author: Anirudh Sharma
"""


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        print("Left:", left)
        print("Right:", right)
        if left[i] < right[j]:
            result.append(left[i])
            i =+ 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    
    
test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Merge Sort:", merge_sort(test))