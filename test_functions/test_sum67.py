import sum67 as test

try1 = [1,2,3,4,5,6,7,8,9,10]
assert 42 == test.sum67(try1)

try2 = [1,2,3,4,5,6,20,21,23,24,25,6,7,8,9,10]
assert 42 == test.sum67(try2)

try3 = [6,20,21,23,24,25,6,7,8,9,10,1,2,3,4,5]
assert 42 == test.sum67(try3)

try4 = [6,7,6,7,8,9,10,1,2,3,4,5]
assert 42 == test.sum67(try4)

try5 = [8,9,10,1,2,3,4,5,6,7,6,7]
assert 42 == test.sum67(try5)

try6 = [6,5,7]
assert 0 == test.sum67(try6)

try7 = [6,5,7,5]
assert 5 == test.sum67(try7)