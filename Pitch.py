class Pitch:
    pitch_char = ''
    pitch_type = 0
    modifiers = None
    # 1 for strike, 2 for foul, 3 for ball, 4 for put into play, 5 for hit by pitcher, 6 no pitch

    def __init__(self, pitch_char=''):
        self.pitch_char = pitch_char
        pitch_char = pitch_char.upper()
        if pitch_char == 'C' or pitch_char == 'K' or pitch_char == 'Q' or pitch_char == 'S' or pitch_char == 'M':
            self.pitch_type = 1
        elif pitch_char == 'F' or pitch_char == 'L' or pitch_char == 'O' or pitch_char == 'R' or pitch_char == 'T':
            self.pitch_type = 2
        elif pitch_char == 'B' or pitch_char == 'I' or pitch_char == 'P' or pitch_char == 'V':
            self.pitch_type = 3
        elif pitch_char == 'X' or pitch_char == 'Y':
            self.pitch_type = 4
        elif pitch_char == 'H':
            self.pitch_type = 5
        elif pitch_char == 'N' or pitch_char == '1' or pitch_char == '2' or pitch_char == '3' or pitch_char == '.':
            self.pitch_type = 6
        else:
            self.pitch_type = 0

        self.modifiers = []

    def addModifier(self, mod):
        self.modifiers.append(mod)
