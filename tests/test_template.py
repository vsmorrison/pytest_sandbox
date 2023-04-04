import pytest


def test_something(some_fixture):
    assert some_fixture == 2


@pytest.mark.xfail(reason="negative test")
@pytest.mark.parametrize("some_value, some_result", ["12"])
def test_parametrization(some_value, some_result):
    assert some_value == some_result

