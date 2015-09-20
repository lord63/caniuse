#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
from click.testing import CliRunner

from caniuse.main import check
from caniuse.cli import cli


class TestAPI():
    def test_package_name_has_been_used(self):
        assert 'Sorry' in check('requests')
        assert 'Sorry' in check('flask')
        assert 'Sorry' in check('pip')

    def test_package_name_has_not_been_used(self):
        assert 'Congratulation' in check('this_package_name_has_not_been_used')
        assert 'Congratulation' in \
            check('you_will_never_use_this_package_name')
        assert 'Congratulation' in \
            check('I_suck_and_my_tests_are_order_dependent')


class TestCLI():
    def test_package_name_has_been_used(self):
        runner = CliRunner()
        result_one = runner.invoke(cli, ['requests'])
        assert 'Sorry' in result_one.output

        result_two = runner.invoke(cli, ['flask'])
        assert 'Sorry' in result_two.output

        result_three = runner.invoke(cli, ['pip'])
        assert 'Sorry' in result_three.output

    def test_package_name_has_not_been_used(self):
        runner = CliRunner()
        result_one = runner.invoke(
            cli, ['this_package_name_has_not_been_used'])
        assert 'Congratulation' in result_one.output

        result_two = runner.invoke(
            cli, ['you_will_never_use_this_package_name'])
        assert 'Congratulation' in result_two.output

        result_three = runner.invoke(
            cli, ['I_suck_and_my_tests_are_order_dependent'])
        assert 'Congratulation' in result_three.output
