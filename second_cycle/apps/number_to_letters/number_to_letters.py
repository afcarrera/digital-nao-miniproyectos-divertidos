class NumberToLetters(object):
    
    def __init__(self):
        self.MAX_NUMBER = 999999999999
        self.UNITS = (
            'cero',
            'uno',
            'dos',
            'tres',
            'cuatro',
            'cinco',
            'seis',
            'siete',
            'ocho',
            'nueve'
        )

        self.TENS = (
            'diez',
            'once',
            'doce',
            'trece',
            'catorce',
            'quince',
            'dieciseis',
            'diecisiete',
            'dieciocho',
            'diecinueve'
        )

        self.TEN_TEN = (
            'cero',
            'diez',
            'veinte',
            'treinta',
            'cuarenta',
            'cincuenta',
            'sesenta',
            'setenta',
            'ochenta',
            'noventa'
        )

        self.HUNDREDS = (
            '_',
            'ciento',
            'doscientos',
            'trescientos',
            'cuatroscientos',
            'quinientos',
            'seiscientos',
            'setecientos',
            'ochocientos',
            'novecientos'
        )

    def number_to_letters(self, number):
        int_number = int(number)
        if int_number > self.MAX_NUMBER:
            raise OverflowError('Número demasiado alto')
        if int_number < 0:
            return 'menos %s' % self.number_to_letters(abs(number))
        letters_decimal = ''
        decimal_part = int(round((abs(number) - abs(int_number)) * 100))
        if decimal_part > 9:
            letters_decimal = 'punto %s' % self.number_to_letters(decimal_part)
        elif decimal_part > 0:
            letters_decimal = 'punto cero %s' % self.number_to_letters(decimal_part)
        if (int_number <= 99):
            result = self.read_tens(int_number)
        elif (int_number <= 999):
            result = self.read_hundreds(int_number)
        elif (int_number <= 999999):
            result = self.read_thousands(int_number)
        elif (int_number <= 999999999):
            result = self.read_millons(int_number)
        else:
            result = self.read_billions(int_number)
        result = result.replace('uno mil', 'un mil')
        result = result.strip()
        result = result.replace(' _ ', ' ')
        result = result.replace('  ', ' ')
        if decimal_part > 0:
            result = '%s %s' % (result, letters_decimal)
        return result

    def read_tens(self, number):
        if number < 10:
            return self.UNITS[number]
        ten, unit = divmod(number, 10)
        if number <= 19:
            result = self.TENS[unit]
        elif number <= 29:
            result = 'veinti%s' % self.UNITS[unit]
        else:
            result = self.TEN_TEN[ten]
            if unit > 0:
                result = '%s y %s' % (result, self.UNITS[unit])
        return result

    def read_hundreds(self, number):
        hundred, ten = divmod(number, 100)
        if number == 0:
            result = 'cien'
        else:
            result = self.HUNDREDS[hundred]
            if ten > 0:
                result = '%s %s' % (result, self.read_tens(ten))
        return result

    def read_thousands(self, number):
        thousand, hundred = divmod(number, 1000)
        result = ''
        if (thousand == 1):
            result = ''
        if (thousand >= 2) and (thousand <= 9):
            result = self.UNITS[thousand]
        elif (thousand >= 10) and (thousand <= 99):
            result = self.read_tens(thousand)
        elif (thousand >= 100) and (thousand <= 999):
            result = self.read_hundreds(thousand)
        result = '%s mil' % result
        if hundred > 0:
            result = '%s %s' % (result, self.read_hundreds(hundred))
        return result

    def read_millons(self, number):
        millon, thousand = divmod(number, 1000000)
        result = ''
        if (millon == 1):
            result = ' un millon '
        if (millon >= 2) and (millon <= 9):
            result = self.UNITS[millon]
        elif (millon >= 10) and (millon <= 99):
            result = self.read_tens(millon)
        elif (millon >= 100) and (millon <= 999):
            result = self.read_hundreds(millon)
        if millon > 1:
            result = '%s millones' % result
        if (thousand > 0) and (thousand <= 999):
            result = '%s %s' % (result, self.read_hundreds(thousand))
        elif (thousand >= 1000) and (thousand <= 999999):
            result = '%s %s' % (result, self.read_thousands(thousand))
        return result

    def read_billions(self, number):
        billion, millon = divmod(number, 1000000)
        return '%s millones %s' % (self.read_thousands(billion), self.read_millons(millon))