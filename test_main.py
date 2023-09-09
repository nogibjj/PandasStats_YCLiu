from main import addNum

def test_func():
    assert addNum(1, 2) == 3
    assert addNum(1, -1) == 0
    assert addNum(0, -2) == -2