import lone_sum as test

def test_lone_sum_1():
    assert 6 == test.lone_sum(1,2,3)

def test_lone_sum_2():
    assert 20 == test.lone_sum(5,13,2)

def test_lone_sum_3():
    assert 29 == test.lone_sum(14,13,2)

def test_lone_sum_4():
    assert 45 == test.lone_sum(14,13,18)

def test_lone_sum_5():
    assert 26 == test.lone_sum(8,16,2)

def test_lone_sum_6():
    assert 27 == test.lone_sum(8,17,2)

def test_lone_sum_7():
    assert 28 == test.lone_sum(8,18,2)

def test_lone_sum_8():
    assert 29 == test.lone_sum(8,19,2)

def test_lone_sum_9():
    assert 30 == test.lone_sum(8,20,2)

def test_lone_sum_10():
    assert 20 == test.lone_sum(2,20,2)

def test_lone_sum_11():
    assert 0 == test.lone_sum(2,2,2)

def test_lone_sum_12():
    assert 20 == test.lone_sum(2,2,20)

def test_lone_sum_13():
    assert 20 == test.lone_sum(20,2,2)