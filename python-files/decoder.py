# decoder.py

import numpy as np
from rtlsdr import RtlSdr

from constants import centr_freq, sample_rate, gain
from preamble_detection import findPreambleIndices
from bit_extraction import samples_to_bits
from frame_parser import parseFrame


def create_sdr():
    sdr = RtlSdr()
    sdr.sample_rate = sample_rate
    sdr.center_freq = centr_freq
    sdr.gain = gain
    return sdr


def process_block(samples: np.ndarray):
    indices = findPreambleIndices(samples, sample_rate)
    for idx in indices:
        bits = samples_to_bits(samples, idx)
        if len(bits) == 112:
            frame = parseFrame(bits)
            print("Decoded frame:", frame)


def main():
    sdr = create_sdr()
    try:
        print("Reading samples from SDR...")
        samples = np.array(sdr.read_samples(256 * 1024))
        process_block(samples)
    finally:
        sdr.close()
        print("SDR closed.")


if __name__ == "__main__":
    main()

