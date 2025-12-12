# load_capture.py

import numpy as np

# Function to load IQ samples from a rtl_sdr .iq file
def load_iq_file(path: str) -> np.ndarray:
    """
    Load rtl_sdr file (unsigned 8 bit IQ interleaved) as complex samples.
    """
    # Read raw uint8 data from file
    raw = np.fromfile(path, dtype=np.uint8)
    # Convert to complex64: I + jQ, centered around 0
    I = raw[0::2].astype(np.float32) - 127.5
    Q = raw[1::2].astype(np.float32) - 127.5
    # Combine I and Q into complex samples
    return I + 1j * Q

# Test the function
def main():
    path = "../captures/adsb_200k.iq"
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} IQ samples from {path}")

if __name__ == "__main__":
    main()

