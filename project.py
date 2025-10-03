
class py_solution:
    def int_to_Roman(self,num):
        val = [
            1000, 900, 800, 700, 600, 500,
            400, 300, 200, 100, 90, 80, 70, 60, 50,
            40, 30, 20, 10, 9, 8, 7, 6, 5, 4,
            3, 2, 1
              ]
        syb = [
            "M", "CM", "DCCC", "DCC", "DC", "D",
            "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX", "L",
            "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV",
            "III", "II", "I"
              ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
                i += 1
            return roman_num
    
print(py_solution().int_to_Roman(5))
print(py_solution().int_to_Roman(40))
    