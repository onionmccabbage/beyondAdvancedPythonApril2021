import doctest

def cubes(a,b):
    """
    return all the cubes in range a...b
    >>> cubes(1,3)
    [1, 8, 27]
    >>> cubes(1, 100) # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 8, ..., 1000000]
    """
    answers = []
    for i in range(a, b+1):
        answers.append(i*i*i)
    return answers

if __name__ == '__main__':
    # print(cubes(1,3))
    doctest.testmod(verbose=True)