def numtochex(r, g, b):
    """
    Convert RGB values to a hex string.
    :param r: The red value.
    :param g: The green value.
    :param b: The blue value.
    :return: A hex string representing the RGB values.
    """
    return "{:02X}{:02X}{:02X}".format(r, g, b)

def chextonum(hex):
    """
    Convert a hex string to RGB values.
    :param hex: A hex string representing RGB values.
    :return: A tuple (R, G, B) of the RGB values.
    """
    return int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)
