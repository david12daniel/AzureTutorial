import sum13 as test

def test_sum13_1():
    try1 = [1,2,3,4,5,8,9,10,13]
    assert 42 == test.sum13(try1)

def test_sum13_2():
    try2 = [13,1,2,3,4,5,8,9,10]
    assert 41 == test.sum13(try2)

def test_sum13_3():
    try3 = [8,13,9,10,1,2,3,4,5]
    assert 33 == test.sum13(try3)

def test_sum13_4():
    try4 = [13,8,9,10,13,1,2,3,4,5]
    assert 33 == test.sum13(try4)

def test_sum13_5():
    try5 = [8,9,10,13,13,13,1,2,3,4,5]
    assert 41 == test.sum13(try5)

def test_sum13_6():
    try6 = [13,13,6,5,7]
    assert 12 == test.sum13(try6)

def test_sum13_7():
    try7 = [13,13]
    assert 0 == test.sum13(try7)

def test_sum13_8():
    try8 = [0,0]
    assert 0 == test.sum13(try8)

def test_sum13_9():
    try9 = [0]
    assert 0 == test.sum13(try9)

def test_sum13_10():
    try10 = [13]
    assert 0 == test.sum13(try10)

def test_sum13_11():
    try11 = [1]
    assert 1 == test.sum13(try11)