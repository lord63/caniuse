# caniuse

[![Latest Version][1]][2]
[![Build Status][3]][4]
[![Wheel Status][5]][6]

> Can I use this name for my python package on PyPI?

check whether a package name has been used on PyPI.

## Install

    $ pip install caniuse

## Usage

### API

    >>> from caniuse.main import check
    >>> check('requests')
    u'Sorry, this package name has been registered :(\nHave a look at it: http://pypi.python.org/pypi/requests'
    >>>
    >>> check('you_will_never_use_this_name')
    u'Congratulations! You can use it :)'

### CLI

    $ caniuse requests
    Sorry, this package name has been registered :(
    Have a look at it: http://pypi.python.org/pypi/requests

    $ caniuse you_will_never_use_this_name
    Congratulations! You can use it :)

## Tests

    $ pip install -r dev-requirements.txt
    $ make test

### License

MIT.

[1]: http://img.shields.io/pypi/v/caniuse.svg
[2]: https://pypi.python.org/pypi/caniuse
[3]: https://travis-ci.org/lord63/caniuse.svg
[4]: https://travis-ci.org/lord63/caniuse
[5]: https://img.shields.io/badge/wheel-yes-blue.svg
[6]: https://img.shields.io/badge/wheel-yes-blue
