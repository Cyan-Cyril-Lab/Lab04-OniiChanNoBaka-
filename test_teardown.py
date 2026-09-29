import pytest

@pytest.fixture
def setup_teardown():
    print("[setup]")
    yield
    print("[teardown]")

def test_one(setup_teardown):
    assert True

def test_two(setup_teardown):
    assert True