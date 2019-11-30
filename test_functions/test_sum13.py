import sum13 as test

try1 = [1,2,3,4,5,8,9,10,13]
assert 42 == test.sum13(try1)

try2 = [13,1,2,3,4,5,8,9,10]
assert 41 == test.sum13(try2)

try3 = [8,13,9,10,1,2,3,4,5]
assert 33 == test.sum13(try3)

try4 = [13,8,9,10,13,1,2,3,4,5]
assert 33 == test.sum13(try4)

try5 = [8,9,10,13,13,13,1,2,3,4,5]
assert 41 == test.sum13(try5)

try6 = [13,13,6,5,7]

print(test.sum13(try6))
assert 12 == test.sum13(try6)

try7 = [13,13]
assert 0 == test.sum13(try7)

try8 = [0,0]
assert 0 == test.sum13(try8)

try9 = [0]
assert 0 == test.sum13(try9)

try10 = [13]
assert 0 == test.sum13(try10)

try11 = [1]
assert 1 == test.sum13(try11)