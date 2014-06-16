"""Implemements the spacing algorithm.

"""

def interval(repetition, rating, easy_factor=2.5):
    """Simplified SM-2 spacing algorithm.

    It is loosely based on the SuperMemo 2 algorithm. Details at:
        http://www.supermemo.com/english/ol/sm2.htm

    Args:
     repetition (int): Number of repetitions until now.
     rating (int): Difficulty rating for the item in question. From 0 (hardest) to 4 (easiest).
     easy_factor (float): An factor for calculating the next

    Returns:
      int: minutes until next practice
      float: new easiness factor

    """
    if rating < 3:
        return 10, easy_factor
    elif rating == 3:
        return 30, easy_factor
    else:
        repetition, easy_factor = calculateEasyFactor(easy_factor, rating, repetition)
        repetition_interval = calculateInterval(repetition, rating, easy_factor)
        repetition_interval *= 1440 # delay() expects the interval in minutes, but calculateInterval() returns days.
        return repetition_interval, easy_factor

def calculateInterval(repetition, rating, easy_factor):
    """ Calculate the inter-repetition interval

        I(1):= r/2
        I(2):= r
        for n>2 I(n):=I(n-1)*EF

    where:
        I(n) - inter-repetition interval after the n-th repetition (in days)
        EF - easiness factor reflecting the easiness of memorizing and retaining a given item in memory.
        r - Rating, given by the user.

    The calculation is done recursively. Details at:
        http://www.supermemo.com/english/ol/sm2.htm

    The deviation from SM-2 consists in the following details:
        - The default interval for the first and second repetition is not fixed to 1 and 6, but relative to
          the user rating.

    Args:
     repetition (int): Number of repetitions until now.
     easy_factor (float): easiness factor

    Returns:
      int: days until next practice

    """
    if repetition < 0:
        raise ValueError, 'Repetition must be 0 at least!'

    if easy_factor < 1.3:
        raise ValueError, 'Easy factor must not be less than 1.3!'

    if repetition < 3:
        return rating/2
    elif repetition==3:
        return rating
    else:
        return calculateInterval(repetition-1, rating, easy_factor)*easy_factor

def calculateEasyFactor(oldEF, rating, repetition):
    """ Calculate new easy factor from old factor and rating.

     EF' := f(EF,q)
     where,
         EF' = new value of the easiness factor
         EF  = old value of the easiness factor
         q   = user difficulty rating (1-4)
         f(EF,q)   = EF-0.8+0.28*q-0.02*q*q

    Args:
     oldEF (float): An factor for calculating the next repetition interval.
     rating (int): Difficulty rating for the item in question. From 0 (impossible) to 5 (easiest).
     repetition (int): Number of repetitions until now.

    Returns:
      int: minutes until next practice
      float: new easiness factor

    """
    if oldEF < 1.3:
        raise ValueError, 'Easy factor must not be less than 1.3!'

    if rating not in xrange(0,6):
        raise ValueError, 'Rating must be positive and less than 6!'

    # If the card is rated < 2, the number of repetitions is reset.
    if rating < 2:
        repetition = 1

    # Calculate new easy facor using the SM-2 formula.
    newEF = oldEF - 0.8 + 0.28 * rating - 0.02 * rating * rating
    if newEF < 1.3:
        newEF=1.3

    return repetition, newEF