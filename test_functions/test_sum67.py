import sum67 as test

def test_sum67_1():
    try1 = [1,2,3,4,5,6,7,8,9,10]
    assert 42 == test.sum67(try1)

def test_sum67_2():
    try2 = [1,2,3,4,5,6,20,21,23,24,25,6,7,8,9,10]
    assert 42 == test.sum67(try2)

def test_sum67_3():
    try3 = [6,20,21,23,24,25,6,7,8,9,10,1,2,3,4,5]
    assert 42 == test.sum67(try3)

def test_sum67_4():
    try4 = [6,7,6,7,8,9,10,1,2,3,4,5]
    assert 42 == test.sum67(try4)

def test_sum67_5():
    try5 = [8,9,10,1,2,3,4,5,6,7,6,7]
    assert 42 == test.sum67(try5)

def test_sum67_6():
    try6 = [6,5,7]
    assert 0 == test.sum67(try6)

def test_sum67_7():
    try7 = [6,5,7,5]
    assert 5 == test.sum67(try7)