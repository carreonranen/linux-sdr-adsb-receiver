# payload_decoder.py

def get_type_code(rawM: int) -> int:
    # top 5 bits of the 56 bit ME field
    return (rawM >> 51) & 0b11111


def classify_type_code(tc: int) -> str:
    if 1 <= tc <= 4:
        return "Aircraft Identification"
    elif 5 <= tc <= 8:
        return "Surface Position(Ground Movement)"
    elif 9 <= tc <= 18:
        return "Airborne Position"
    elif tc == 19:
        return "Airborne Velocity"
    elif 23 <= tc <= 27:
        return "Reserved/Test"
    elif 28 <= tc <= 31:
        return "Status/Other"
    else:
        return "Unknown"


def summarize_payload(rawM: int) -> dict:
    tc = get_type_code(rawM)
    return {
        "tc": tc,
        "category": classify_type_code(tc),
    }

