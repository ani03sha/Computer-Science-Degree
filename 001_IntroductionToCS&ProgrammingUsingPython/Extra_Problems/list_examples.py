"""
@author: Anirudh Sharma
"""

# Example #1

def sum_of_list_elements(L):
    total = 0 
    for i in L: 
        total += L[i - 1] 
    return total

L = [1, 2, 3, 4, 5, 6]
print(sum_of_list_elements(L))


# Example #2

def list_operations(L1, L2):
    L3 = L1 + L2
    print("L1 + L2: ", L3)
    
    L1.remove(2)
    L2.remove(6)
    print("Mutated L1 after remove:", L1)
    print("Mutated L2 after remove:", L2)
    
    L1.append(7)
    L2.append(9)
    print("Mutated L1 after add: ", L1)
    print("Mutated L2 after add:", L2)
    
    del(L1[1])
    print("Mutated L1 after deleting element at index 1:", L1)
    
    print("Popping from L2: ", L2.pop())


L1 = [1, 2, 3]
L2 = [4, 5, 6]
list_operations(L1, L2)


# Example #3

def string_and_list_manipulations(L, s):
    # Convert string to list
    print(list(s))
    print(s.split(' '))
    # Convert list to string
    print(''.join(L))
    print('_'.join(L))
    
s = "I <3 CS"
L = ['A', 'n', 'i', 'r', 'u', 'd', 'h']
string_and_list_manipulations(L, s)


# Example #4

def more_list_operations(L1, L2):
    L.sort()
    print("Sorted but mutated list:", L)
    print("Sorted but immutable list:", sorted(L))
    # Reverse the list
    L.reverse()
    print("Reversed List:", L)
    
L1 = [5, 8, -9, -1, 3]
L2 = [5, 8, -9, -1, 3]
more_list_operations(L1, L2)


# Example #5

def aliasing(L):
    newL = L
    print("L:", L)
    print("New L:", newL)
    newL.append("Five")
    print("L after appending in newL:", L)
    print("New L after appending in newL:", newL)

L = ["One", "Two", "Three", "Four"]
aliasing(L)


# Example #6

def cloning(L):
    newL = L[:]
    print("L:", L)
    print("New L:", newL)
    newL.append("Five")
    print("L after appending in newL:", L)
    print("New L after appending in newL:", newL)
    
L = ["One", "Two", "Three", "Four"]
cloning(L)


# Example #7

def list_of_list():
    warm = ["orange", "yellow"]
    hot = ["red"]
    bright = [warm]
    print(bright)
    bright.append(hot)
    print(bright)
    hot.append("pink")
    print(hot)
    print(bright)
    
    
list_of_list()


# Example # 8

def remove_duplicates(L1, L2):
    L1_copy = L1[:]
    for i in L1_copy:
        if i in L2:
            L1.remove(i)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_duplicates(L1, L2)
print(L1, L2)