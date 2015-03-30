ELEMENTS = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def checkio(number):
    result = ""
    for roman, n in ELEMENTS:
        if n <= number:
            result += roman * (number // n)
            number %= n
    return result

for i in range(1, 4000):
    print(i, checkio(i))
