#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import click

from caniuse.main import check
from caniuse import __version__


@click.command(context_settings={'help_option_names': ('-h', '--help')})
@click.argument('name')
@click.version_option(__version__, '-V', '--version', message='%(version)s')
def cli(name):
    click.echo(check(name))
