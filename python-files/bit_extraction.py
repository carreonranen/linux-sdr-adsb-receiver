# bit_extraction.py

import numpy as np
from constants import sample_rate, bit_period, preamble, data_bits


def samples_to_bits(samples, preamble_index):
    """
    Convert complex samples to a list of ADS-B bits using a simple PPM test.
    """

    # at 2 MS/s and 1 Mbps this should be ~2 samples per bit
    samples_per_bit = int(round(sample_rate * bit_period))

    # preamble is in bit periods
    preamble_samples = int(round(preamble * bit_period * sample_rate))

    data_start = preamble_index + preamble_samples
    needed = data_start + data_bits * samples_per_bit

    if needed > len(samples):
        return []

    mag = np.abs(samples)
    bits = []

    for n in range(data_bits):
        start = data_start + n * samples_per_bit

        i0 = start
        i1 = start + 1

        if i1 >= len(mag):
            break

        chip0 = mag[i0]
        chip1 = mag[i1]

        # early pulse means 1, late pulse means 0
        bits.append(1 if chip0 > chip1 else 0)

    return bits

