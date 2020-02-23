# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations(list(sequence), 0, len(sequence) - 1)

def permutations(sequence, start, end):
    # Base condition
    if(start == end):
        print(''.join(sequence))
        return
    
    for i in range(start, end + 1):
        sequence[start], sequence[i] = sequence[i], sequence[start]
        permutations(sequence, start + 1, end)
        # Backtrack like a tree to restore previous state
        sequence[start], sequence[i] = sequence[i], sequence[start]
        

if __name__ == '__main__':
    s = 'abc'
    get_permutations(s)