import numpy as np
from load_capture import load_iq_file
from preamble_detection import findPreambleIndices
from constants import sample_rate


def main() -> None:
    path = "../captures/adsb_200k.iq"
    print(f"Loading samples from {path}...")
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} samples.")

    print("Running preamble detection...")
    idx = findPreambleIndices(samples, sample_rate)

    print(f"Found {len(idx)} candidate pulses.")
    print("First 20 indices:", idx[:20])


if __name__ == "__main__":
    main()

