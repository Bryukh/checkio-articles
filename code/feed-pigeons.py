def checkio(portions):
    """Simple and straight"""
    fed = 0
    minute = 0
    pigeons = 0
    while portions >= 0:
        portions -= pigeons
        minute += 1
        if portions <= 0:
            return fed
        if minute < portions:
            fed += minute
            portions -= minute
        else:
            fed += portions
            return fed
        pigeons += minute
    return fed


print([checkio(i) for i in range(50)])