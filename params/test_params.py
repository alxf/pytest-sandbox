# -*- coding: utf-8 -*-

""" Test parameters from a yaml file """

import io
import os
import yaml


datafile = 'params.yaml'


def pytest_generate_tests(metafunc):
    """ Generate input data from yaml file. If a fixture has
        the same name than a key in the yaml data source, it
        will load it as params.

        metafunc -- the test function to parametrize
    """
    datapath = os.path.join(
        os.path.dirname(__file__),
        datafile
    )
    with io.open(datapath, 'rb') as fd:
        data = yaml.load(fd)
    for key in data.keys():
        if key in metafunc.fixturenames:
            metafunc.parametrize(key, [item for item in data[key]])


def test_add_ab(a, b):
    """ Test the addition of a and b.
    """
    assert(a + b)


def test_add_err_ab(err_a, b):
    """ Test the addition of a and b with one string in the params.
    """
    assert(int(err_a) + b)


def test_dict_key(sample_data):
    """ You can pass more complex data structure like dict.
    """
    for k in sample_data:
        assert(k.endswith('dict'))


