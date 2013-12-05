def interval(repetition, rating, easy_factor=2.5):
    """Dummy Implementation of spacing algorithm. Does random stuff.

    """
    if repetition <= 10:
        repetition = 1
    else:
        repetition /= 10
    i = 60*(rating+1) * 2 * repetition
    return i, easy_factor
