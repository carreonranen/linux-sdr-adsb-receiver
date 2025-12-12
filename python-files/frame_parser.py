# frame_parser.py

from bitstring import BitArray

# Function to parse a 112 bit ADS-B frame into its components
def parseFrame(bits):
    """
    Split a 112 bit ADS-B frame into basic fields.
    """
    # Validate input length
    if len(bits) != 112:
        raise ValueError("ADS-B frame must have 112 bits")
    # Convert bits to BitArray for easy slicing
    b = BitArray(bits=bits)

    # Extract fields based on ADS-B frame structure
    df = b[0:5].uint
    ca = b[5:8].uint
    icao = b[8:32].uint
    rawM = b[32:88].uint
    rawCRC = b[88:112].uint
    
    # Return parsed fields as a dictionary
    return {
        "df": df,
        "ca": ca,
        "icao": icao,
        "rawM": rawM,
        "rawCRC": rawCRC,
    }

