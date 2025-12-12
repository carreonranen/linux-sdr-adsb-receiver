# decode_identification.py

#This module decodes the aircraft identification(callsign) from the ADS-B message's ME field.
from bitstring import BitArray

#Helper function to map 6-bit values to characters according to ADS-B encoding
def sixbit_to_char(v: int) -> str:
    if v == 0:
        return " "
    if 1 <= v <= 26:
        return chr(ord("A") + v - 1)
    if 48 <= v <= 57:
        return chr(ord("0") + v - 48)
    return " "

# Function to decode callsign from the 56-bit ME field
def decode_callsign(rawM: int) -> str:
    """
    Decode callsign from the 56 bit ME field.
    """

    b = BitArray(uint=rawM, length=56)

    # bits for each 6 bit character
    starts = [8, 14, 20, 26, 32, 38, 44, 50]

    #Extract each 6-bit segment and convert to character
    chars = []
    for s in starts:
        v = b[s : s + 6].uint
        chars.append(sixbit_to_char(v))
    #Join characters to form the callsign string and strip trailing spaces
    return "".join(chars).strip()

