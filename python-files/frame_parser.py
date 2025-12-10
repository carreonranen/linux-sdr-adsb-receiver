# frame_parser.py

from bitstring import BitArray


def parseFrame(bits):
    """
    Split a 112 bit ADS-B frame into basic fields.
    """

    if len(bits) != 112:
        raise ValueError("ADS-B frame must have 112 bits")

    b = BitArray(bits=bits)

    df = b[0:5].uint
    ca = b[5:8].uint
    icao = b[8:32].uint
    rawM = b[32:88].uint
    rawCRC = b[88:112].uint

    return {
        "df": df,
        "ca": ca,
        "icao": icao,
        "rawM": rawM,
        "rawCRC": rawCRC,
    }

