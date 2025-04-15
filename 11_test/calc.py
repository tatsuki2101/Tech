# 2つの整数の加算を行う
def add(a, b):
    return a + b

# 2つの整数の減算を行う
def subtract(a, b):
    return a - b

# 2つの整数の乗算を行う
def multiply(a, b):
    return a * b

# 2つの整数の除算を行う
# ゼロ除算が発生した場合、エラーを返す
def divide(a, b):
    if b == 0:
        raise ValueError("0で除算された")
    return a / b
