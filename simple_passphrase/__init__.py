import random

def generate_passphrase(phrases, number, minimum, sep, max_tries=10, rand=random):
    """Return a string whose len(s) > ``minimum`` with number ``random``
    phrases joined by random characters from ``sep``

    rand -- should provide an interface similar to ``random``, at least
            ``randint`` and ``choice``
    max_tries -- the maximum iterations to try if minimum isn't met

    Raises ValueError if it fails at doing so.

    """
    passphrase = ''
    tries = 0
    while tries < max_tries and len(passphrase) < minimum:
        words = []
        for i in range(number):
            x = rand.randint(0, len(phrases))
            words.append(phrases[x])
        passphrase = sep.join(words)
        tries += 1
    if tries >= max_tries:
        passphrase = ''
    return passphrase, tries
