class Roman_Numeral:
    def __init__(self):
        pass

    def get_roman_numeral(self,value):
        roman_numerals = [
            'M',
            'CM',
            'D',
            'CD',
            'C',
            'XC',
            'L',
            'XL',
            'X',
            'IX',
            'V',
            'IV',
            'I'
        ]

        roman_numeral_values = [
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1
        ]
        
        numeral = ''
        i=0
        while value > 0:
            for _ in range(value//roman_numeral_values[i]):
                numeral+=roman_numerals[i]

            i=i+1

        return numeral


