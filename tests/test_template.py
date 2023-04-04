import pytest


def test_something(some_fixture):
    assert some_fixture == 2


@pytest.mark.parametrize("some_value", "1")
def test_parametrization(some_value):
    assert some_value == 123

