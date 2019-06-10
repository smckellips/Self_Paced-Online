#!/usr/bin/env python

from donor import donor
import pytest

def test_init():
    d = Donor('Abe Froman')
    assert d.name == 'Abe Froman'