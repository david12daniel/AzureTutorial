import has22

def test_has22_1():
    try1 = [1,2,2]
    returnVal = has22.has22(try1)

    assert returnVal == True

def test_has22_2():
    try2 = [2,2,100,1,22,22,2,2,10,2]
    returnVal = has22.has22(try2)

    assert returnVal == True

def test_has22_3():
    try3 = [0]
    returnVal = has22.has22(try3)

    assert returnVal == False

def test_has22_4():
    try4 = [2, 2]
    returnVal = has22.has22(try4)

    assert returnVal == True

def test_has22_5():
    try5 = [2]
    returnVal = has22.has22(try5)

    assert returnVal == False

