def coordinate_translator(cell):
    col, row = cell
    return int(row) - 1, ord(col) - ord("a")


def safe_pawns(pawns):
    safe_count = 0
    for p in pawns:
        if (chr(ord(p[0]) - 1) + chr(ord(p[1]) - 1) in pawns or
                chr(ord(p[0]) + 1) + chr(ord(p[1]) - 1) in pawns):
            safe_count += 1
    return safe_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
