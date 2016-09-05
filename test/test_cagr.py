from cagr import cagr
from nose.tools import assert_almost_equals, assert_raises


def test_exception_on_no_initial_value():
    assert_raises(Exception, cagr, 0, 1, 1)


def test_exception_on_no_time_period():
    assert_raises(Exception, cagr, 1, 1, 0)
    assert_raises(Exception, cagr, 1, 1, None, 0)


def test_no_increase():
    assert_almost_equals(cagr(1000, 1000, 1), 0.0)


def test_one_year():
    assert_almost_equals(cagr(1000, 1100, 1), 0.1)
    assert_almost_equals(cagr(1000, 1100, None, 12), 0.1)


def test_many_years():
    assert_almost_equals(cagr(1000, 2593.7424601, 10), 0.1)
    assert_almost_equals(cagr(1000, 2593.7424601, None, 120), 0.1)


def test_part_of_a_year():
    assert_almost_equals(cagr(1000, 1100, 0.5), 0.21)
    assert_almost_equals(cagr(1000, 1100, None, 6), 0.21)
