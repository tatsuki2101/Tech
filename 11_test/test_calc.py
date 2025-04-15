import pytest
import calc

# 加算関数 add のテスト
def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(-5, -3) == -8
    assert calc.add(7, -2) == 5
    assert calc.add(0, 5) == 5
    assert calc.add(3, 0) == 3

# 減算関数 subtract のテスト
def test_subtract():
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-3, -5) == 2
    assert calc.subtract(7, -2) == 9
    assert calc.subtract(5, 0) == 5
    assert calc.subtract(0, 3) == -3

# 乗算関数 multiply のテスト
def test_multiply():
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, -3) == 6
    assert calc.multiply(2, -3) == -6
    assert calc.multiply(5, 0) == 0
    assert calc.multiply(0, 3) == 0

# 除算関数 divide のテスト
def test_divide():
    assert calc.divide(6, 3) == 2
    assert calc.divide(-6, -3) == 2
    assert calc.divide(6, -3) == -2

# 除算関数 divide が0で除算された場合にエラーを返すことを検証する
def test_divide_by_zero():
    with pytest.raises(ValueError, match="0で除算された"):
        calc.divide(5, 0)
    with pytest.raises(ValueError, match="0で除算された"):
        calc.divide(0, 0)