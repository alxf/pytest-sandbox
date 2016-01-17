# -*- coding: utf-8 -*-

""" Test parameters from a yaml file """

import io
import os
import yaml
import pytest

datafile = 'params.yaml'


def pytest_generate_tests(metafunc):
    """ Generate input data from yaml file. If a fixture has
        the same name than a key in the yaml data source, it
        will load it as params.

        metafunc -- the test function to parametrize
    """
    xfail = lambda item: item['result'] and item['data'] \
                or pytest.mark.xfail(item['data'])

    datapath = os.path.join(
        os.path.dirname(__file__),
        datafile
    )
    with io.open(datapath, 'rb') as fd:
        data = yaml.load(fd)

    for key in data.keys():
        if key in metafunc.fixturenames:
            metafunc.parametrize(
                key,
                [isinstance(item, dict) and xfail(item) or item \
                        for item in data[key]],
            )


def test_add_ab(a, b):
    """ Test the addition of a and b.
    """
    assert(a + b)

def test_no_xfail(s):
    """ Test a list of parameters.
    """
    assert(s)

