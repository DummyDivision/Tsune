"""Implemements the spacing algorithm.

"""

def interval(repetition, rating, easy_factor=2.5):
    """Dummy Implementation of spacing algorithm. Does random stuff.

    This is just a dummy implementation of a spacing algorithm. It is going to be replaced with
    a real algorithm in a future use case. It is loosely based on the SuperMemo 2 algorithm.

    Args:
     repetition (int): Number of repetitions until now.
     rating (int): Difficulty rating for the item in question. From 0 (hardest) to 4 (easiest).
     easy_factor (float): An factor for calculating the next

    Returns:
      int: minutes until next practice
      float: new easyfactor

    """
    if repetition <= 10:
        repetition = 1
    else:
        repetition /= 10
    i = 60*(rating+1) * 2 * repetition
    return i, easy_factor
