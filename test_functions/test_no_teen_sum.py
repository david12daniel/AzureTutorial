import no_teen_sum as test

def test_no_teen_sum_1():
    assert 6 == test.no_teen_sum(1,2,3)

def test_no_teen_sum_2():
    assert 7 == test.no_teen_sum(5,13,2)

def test_no_teen_sum_3():
    assert 2 == test.no_teen_sum(14,13,2)

def test_no_teen_sum_4():
    assert 0 == test.no_teen_sum(14,13,18)

def test_no_teen_sum_5():
    assert 26 == test.no_teen_sum(8,16,2)

def test_no_teen_sum_6():
    assert 10 == test.no_teen_sum(8,17,2)

def test_no_teen_sum_7():
    assert 10 == test.no_teen_sum(8,18,2)

def test_no_teen_sum_8():
    assert 10 == test.no_teen_sum(8,19,2)

def test_no_teen_sum_9():
    assert 30 == test.no_teen_sum(8,20,2)