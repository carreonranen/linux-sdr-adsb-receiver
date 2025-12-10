# load_capture.py

import numpy as np


def load_iq_file(path: str) -> np.ndarray:
    """
    Load rtl_sdr file (unsigned 8 bit IQ interleaved) as complex samples.
    """

    raw = np.fromfile(path, dtype=np.uint8)

    I = raw[0::2].astype(np.float32) - 127.5
    Q = raw[1::2].astype(np.float32) - 127.5

    return I + 1j * Q


def main():
    path = "../captures/adsb_200k.iq"
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} IQ samples from {path}")


if __name__ == "__main__":
    main()

