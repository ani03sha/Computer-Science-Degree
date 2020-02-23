"""
@author: Anirudh Sharma
"""

def gen_subsets(L):
    if len(L) == 0:
        return [[]]
    rest = gen_subsets(L[:-1])
    extra = L[-1:]
    new = []
    for s in rest:
        new.append(rest + extra)
    return rest + new

test = [1, 2, 3, 4]
print(gen_subsets(test))