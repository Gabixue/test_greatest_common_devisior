'''
a = input('a: ')
while not a.isnumeric():
    a = input('a: ')
a = int(a)
b = input('b: ')
while not b.isnumeric():
    b = input('b: ')
b = int(b)
'''
def greatest_common_divisor(a, b):
    # base case
    if b == 0:
        return a
    r = a % b
    return greatest_common_divisor(b, r)

print(greatest_common_divisor(a, b))

# test with pytest
def test_greatest_common_divisor():
    assert greatest_common_divisor(30, 81) == 3

test_greatest_common_divisor()
