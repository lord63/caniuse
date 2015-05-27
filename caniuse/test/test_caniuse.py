#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import pytest

from caniuse.main import check


def test_package_name_has_been_used():
    assert 'Sorry' in check('requests')
    assert 'Sorry' in check('flask')
    assert 'Sorry' in check('pip')


def test_package_name_has_not_been_used():
    assert 'Congratulation' in check('this_package_name_has_not_been_used')
    assert 'Congratulation' in check('you_will_never_use_this_package_name')
    assert 'Congratulation' in check('I_suck_and_my_tests_are_order_dependent')
