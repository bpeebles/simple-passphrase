Simple Passphrases
##################

Very simple package to generate passphrases.

Install
*******

Using ``pip`` should work. Something like::

    $ pip install git+git://github.com/bpeebles/devrandom.git#egg=devrandom
    $ pip install git+git://github.com/bpeebles/simple-passphrase#egg=simple_passphrase

inside of a virtualenv or some such.

Simple Diceware
***************

Included is a ``diceware`` script to generate `Diceware
<http://world.std.com/~reinhold/diceware.html>`_ style passphrases.

This attempts to use my ``devrandom`` `module
<https://github.com/bpeebles/devrandom>`_, then tries to
``random.SystemRandom``, and then falls back to ``random`` if no other source
is there. A warning is issued in the latter two cases.

The Diceware_ site suggest using a physical, dice-based generation method.
Since I know I'll never keep my passphrases *that* secure, I figure I might as
well make creation of the phrases as easy as possible so I'd actually use
something like it.

Help message::

    usage: dicewords [-h] [-m MINIMUM] [-n NUMBER] [-s SEP] [-f PATH] [-v]

    Generate dicewords passphrases

    optional arguments:
    -h, --help            show this help message and exit
    -m MINIMUM, --minimum MINIMUM
                            Minimum number of total characters in passphrase.
    -n NUMBER, --number NUMBER
                            Number of words in dicewords passphrase.
    -s SEP, --seperator SEP
                            Seperation characters between dice words.
    -f PATH, --file PATH  Location of dicewords file, in 'NNNNNN word' format.
                            Defaults to package provided list.
    -v, --verbose


.. _module https://github.com/bpeebles/devrandom
.. _Diceware http://world.std.com/~reinhold/diceware.html
