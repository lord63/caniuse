#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

import pytest
import responses
from click.testing import CliRunner


ROOT = path.join(path.abspath(path.dirname(__file__)), 'responses')


def mock_package_response(name, status_code=200):
    with open(path.join(ROOT, '{0}.json'.format(name))) as f:
        mock_response_body = f.read()
        responses.add(responses.GET,
                      'https://pypi.python.org/pypi/{0}/json'.format(name),
                      body=mock_response_body,
                      content_type='application/json',
                      status=status_code)


@pytest.yield_fixture
def mock_api():
    for package_name in ['requests', 'flask', 'pip']:
        mock_package_response(package_name)
    for package_name in ['this_package_name_has_not_been_used',
                         'you_will_never_use_this_package_name',
                         'I_suck_and_my_tests_are_order_dependent']:
        mock_package_response(package_name, status_code=404)

    responses.start()
    yield responses
    responses.stop()


@pytest.fixture(scope='function')
def runner(mock_api):
    return CliRunner()
