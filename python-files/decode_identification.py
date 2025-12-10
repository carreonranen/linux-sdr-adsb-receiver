# decode_identification.py

from bitstring import BitArray


def _sixbit_to_char(v: int) -> str:
    if v == 0:
        return " "
    if 1 <= v <= 26:
        return chr(ord("A") + v - 1)
    if 48 <= v <= 57:
        return chr(ord("0") + v - 48)
    return " "


def decode_callsign(rawM: int) -> str:
    """
    Decode callsign from the 56 bit ME field.
    """

    b = BitArray(uint=rawM, length=56)

    # bits for each 6 bit character
    starts = [8, 14, 20, 26, 32, 38, 44, 50]

    chars = []
    for s in starts:
        v = b[s : s + 6].uint
        chars.append(_sixbit_to_char(v))

    return "".join(chars).strip()

