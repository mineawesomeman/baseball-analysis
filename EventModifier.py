import Location


def EMfromStr(string):
    number = 0
    eType = 0
    loc = 0
    if string[:2] == "AP":
        eType = 1
        loc = 2
    elif string[:4] == 'BGDP':
        eType = 4
        loc = 4
    elif string[:4] == 'BINT':
        eType = 5
        loc = 4
    elif string[:4] == 'BOOT':
        eType = 7
        loc = 4
    elif string[:4] == 'BPDP':
        eType = 9
        loc = 4
    elif string[:2] == 'BP':
        eType = 2
        loc = 2
    elif string[:2] == 'BG':
        eType = 3
        loc = 2
    elif string[:2] == 'BL':
        eType = 6
        loc = 2
    elif string[:2] == 'BP':
        eType = 8
        loc = 2
    elif string[:2] == 'BR':
        eType = 10
        loc = 2
    elif string[:4] == 'COUB':
        eType = 12
        loc = 4
    elif string[:4] == 'COUF':
        eType = 13
        loc = 4
    elif string[:4] == 'COUR':
        eType = 14
        loc = 4
    elif string[:1] == 'C':
        eType = 11
        loc = 1
    elif string[:2] == 'DP':
        eType = 15
        loc = 2
    elif string[:1] == 'E':
        eType = 16
        loc = 2
        number = int(string[1])
    elif string[:3] == 'FDP':
        eType = 18
        loc = 3
    elif string[:4] == 'FINT':
        eType = 19
        loc = 4
    elif string[:2] == 'FL':
        eType = 20
        loc = 2
    elif string[:2] == 'FO':
        eType = 21
        loc = 2
    elif string[:1] == 'F':
        eType = 17
        loc = 1
    elif string[:3] == 'GDP':
        eType = 23
        loc = 3
    elif string[:3] == 'GTP':
        eType = 24
        loc = 3
    elif string[:1] == 'G':
        eType = 22
        loc = 1
    elif string[:2] == 'IF':
        eType = 25
        loc = 2
    elif string[:3] == 'INT':
        eType = 26
        loc = 3
    elif string[:4] == 'IPHR':
        eType = 27
        loc = 4
    elif string[:3] == 'LDP':
        eType = 29
        loc = 3
    elif string[:3] == 'LTP':
        eType = 30
        loc = 3
    elif string[:1] == 'L':
        eType = 28
        loc = 1
    elif string[:4] == 'MREV':
        eType = 31
        loc = 4
    elif string[:3] == 'NDP':
        eType = 32
        loc = 3
    elif string[:3] == 'OBS':
        eType = 33
        loc = 3
    elif string[:4] == 'PASS':
        eType = 35
        loc = 4
    elif string[:1] == 'P':
        eType = 34
        loc = 1
    elif string[:4] == 'RINT':
        eType = 37
        loc = 4
    elif string[:1] == 'R':
        eType = 36
        loc = 2
        number = int(string[1])
    elif string[:2] == 'SF':
        eType = 38
        loc = 2
    elif string[:2] == 'SH':
        eType = 39
        loc = 2
    elif string[:2] == 'TH':
        eType = 40
        if len(string) > 2:
            number = int(string[2])
        return EventModifier(eType, number)
    elif string[:2] == 'TP':
        eType = 41
        loc = 2
    elif string[:4] == 'UINT':
        eType = 42
        loc = 4
    elif string[:4] == 'UREV':
        eType = 43
        loc = 4
    else:
        eType = 0
        loc = 0

    location = Location.substr_2_loc_val(string, loc)
    if location is not 0:
        location_obj = Location.Location(location)
    else:
        location_obj = None

    if eType == 0 and location_obj is None:
        return None
    return EventModifier(eType, number, location_obj)


class EventModifier:
    location = None
    num = 0  # can be a base number or a player number but is probably 0
    eType = 0

    def __init__(self, eType, num=0, location=None):
        self.eType = eType
        self.location = location
        self.num = num

    def __eq__(self, other):
        return self.eType == other.eType and self.num == other.num and self.location == other.location
