# capture_samples.py

import numpy as np
from rtlsdr import RtlSdr
from constants import centr_freq, sample_rate, gain


def main():
    sdr = RtlSdr()

    try:
        sdr.sample_rate = sample_rate
        sdr.center_freq = centr_freq
        sdr.gain = gain

        # change this if you want a longer capture
        capture_seconds = 1.0
        num_samples = int(sample_rate * capture_seconds)

        print(f"Capturing {capture_seconds} s of samples...")
        samples = np.array(sdr.read_samples(num_samples))

        print(f"Captured {len(samples)} samples")

        out_path = "../captures/adsb_capture.npy"
        np.save(out_path, samples)
        print(f"Saved capture to {out_path}")
    finally:
        sdr.close()
        print("SDR stopped and closed")


if __name__ == "__main__":
    main()

