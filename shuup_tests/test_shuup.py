# shuup_tests/test_dummy.py

import pytest

def test_dummy_pass():
    assert True

@pytest.mark.parametrize("value", [1, 2, 3])
def test_multiple_cases(value):
    assert value in [1, 2, 3]

def test_fake_logic():
    result = 2 + 2
    assert result == 4

class TestSampleClass:
    def test_method(self):
        assert "shuup".islower()

    def test_upper(self):
        assert "SHUUP".isupper()

def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
