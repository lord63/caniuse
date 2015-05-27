#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import click

from caniuse.main import check


@click.command()
@click.argument('name')
def cli(name):
    click.echo(check(name))
