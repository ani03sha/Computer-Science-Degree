"""
@author Anirudh Sharma
"""


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
    if len(sequence) == 1:
        return [sequence]
    result = []
    for i, let in enumerate(sequence):
        for p in get_permutations(sequence[:i] + sequence[i + 1:]):
            result = result + [let + p]
    return result


if __name__ == '__main__':
    s = 'abc'
    print(get_permutations(s))