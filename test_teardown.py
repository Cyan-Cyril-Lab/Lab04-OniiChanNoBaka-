import pytest


@pytest.fixture
def setup_teardown():
    print("[setup]")
    yield
    print("[teardown]")


def test_first(setup_teardown):
    assert True


def test_second(setup_teardown):
    assert True