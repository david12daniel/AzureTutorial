import roman_numeral

def test_roman_numeral_1():
    rn=roman_numeral.Roman_Numeral()
    assert 'M' == rn.get_roman_numeral(1000)

def test_roman_numeral_2():
    rn=roman_numeral.Roman_Numeral()
    assert 'CMXII' == rn.get_roman_numeral(912)

def test_roman_numeral_3():
    rn=roman_numeral.Roman_Numeral()
    assert 'MMXIX' == rn.get_roman_numeral(2019)