import numpy as np
from typing import List
from constants import sample_rate, bit_period, preamble, data_bits


def findPreambleIndices(samples: np.ndarray, sample_rate: int) -> List[int]:
    """
    Very simple ADS B preamble detector.
    Returns a list of sample indices where a preamble might start.
    """

    mag = np.abs(samples)

    # rough noise level and threshold
    noise_floor = np.median(mag)
    threshold = noise_floor * 1.8

    # estimate how many samples one full frame takes
    frame_time = (preamble + data_bits) * bit_period
    samples_per_frame = int(frame_time * sample_rate)
    min_gap = max(100, samples_per_frame // 2)

    # local peaks over threshold
    peak_idx: List[int] = []
    for i in range(1, len(mag) - 1):
        if mag[i] > threshold and mag[i] > mag[i - 1] and mag[i] > mag[i + 1]:
            peak_idx.append(i)

    # keep peaks that are far enough apart
    preamble_idx: List[int] = []
    last = -min_gap

    for idx in peak_idx:
        if idx - last >= min_gap:
            preamble_idx.append(idx)
            last = idx

    return preamble_idx

