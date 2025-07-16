def inc(x):
    return x + 1


# def test_answer():
#     assert inc(6) == 7


def add(a, b):
    return a + b


res = add(4, 5)
print("Addition is : ", format(res))


def is_valid(a):
    return bool(a)


res = is_valid(5 > 6)
print("Value is : ", format(res))
