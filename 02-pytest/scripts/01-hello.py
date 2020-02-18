import pytest

def test_hello():
    print("hello world")
    assert 1

if __name__ == '__main__':
    pytest.main(["-s","01-hello.py"])