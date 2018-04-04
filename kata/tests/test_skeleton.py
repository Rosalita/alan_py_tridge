#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from kata.skeleton import fib

__author__ = "Rosie Hamilton"
__copyright__ = "Rosie Hamilton"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
