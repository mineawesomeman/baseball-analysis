locations = ['', '2F', '2', '25F', '25', '1S', '23', '23F', '5S', '56S', '15', '1', '13', '34S', '3S', '6S', '6MS',
             '4MS', '4S', '5F', '5', '56', '6', '6M', '4M', '4', '34', '3', '3F', '5DF', '5D', '56D', '6D', '6MD',
             '4MD', '4D', '34D', '3D', '3DF', '7LSF', '7LS', '7S', '78S', '8S', '89S', '9S', '9LS', '9LSF', '7LF',
             '7L', '7', '78', '8', '89', '9', '9L', '9LF', '7LDF', '7LD', '7D', '78D', '8D', '89D', '9D', '9LD', '9LDF',
             '78XD', '8XD', '89XD']


# returns the loc_val followed by the location where the rest of the string continues
def substr_2_loc_val(inp, start=0):
    longest_length = 0
    ans = 0
    toLook = inp[start:]

    for loc, loc_str in enumerate(locations):
        if toLook[:len(loc_str)] == loc_str and len(loc_str) > longest_length:
            longest_length = len(loc_str)
            ans = loc

    return ans


class Location:
    loc_val = 0

    def __init__(self, loc_val):
        if int(loc_val) == loc_val:
            self.loc_val = loc_val
        else:
            self.loc_val = substr_2_loc_val(loc_val)

    def __eq__(self, other):
        return self.loc_val == other.loc_val

    def __str__(self):
        return locations[self.loc_val]
