#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import requests


def check(package_name):
    response = requests.get(
        'https://pypi.python.org/pypi/{0}/json'.format(package_name))
    try:
        package_url = response.json()['info']['package_url']
        return ("Sorry, this package name has been registered :(\n"
                "Have a look at it: {0}".format(package_url))
    except ValueError:
        return "Congratulations! You can use it :)"
