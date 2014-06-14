import random

def generate_passphrase(phrases, number, minimum, sep, max_tries=10, rand=random):
    """Return a string whose len(s) > ``minimum`` with number ``random``
    phrases joined by random characters from string ``sep``.

    rand -- should provide an interface similar to ``random``, at least
            ``randint`` and ``choice``
    max_tries -- the maximum iterations to try if minimum isn't met



    Raises ValueError if it fails at doing so.

    """
    passphrase = u''
    tries = 0
    while tries < max_tries and len(passphrase) < minimum:
        words = []
        for i in range(number):
            x = rand.randint(0, len(phrases))
            words.append(phrases[x])
        passphrase = u''
        if len(words) > 1:
            for word in words[0:-1]:
                passphrase += word + rand.choice(sep)
        passphrase += word[-1]
        tries += 1
    if tries >= max_tries:
        passphrase = u''
    return passphrase, tries
