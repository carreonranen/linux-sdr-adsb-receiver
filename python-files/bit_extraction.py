# bit_extraction.py

import numpy as np
from constants import sample_rate, bit_period, preamble, data_bits


def samples_to_bits(samples, preamble_index):
    """
    Convert complex samples to a list of ADS-B bits using a simple PPM test.
    """

    # at 2 MS/s and 1 Mbps this should be ~2 samples per bit
    #Converts time into samples. For example if the sample rate is 2mill per sec, bit period is 1x10^-6
    # then 2*1x10^-6 = 2 samples per bit. Tells us how wide each bit windopw is in array
    #Rount it because can't have fractional samples
    samples_per_bit = int(round(sample_rate * bit_period))

    # preamble is in bit periods
    preamble_samples = int(round(preamble * bit_period * sample_rate))


    #This is where the data starts in the samples array. Once I find the preamble(signal waveform), I have to
    # skip past it to get to the data bits which is at its tail end
    data_start = preamble_index + preamble_samples
    needed = data_start + data_bits * samples_per_bit

    #Failsafe to prevent reading past end of samples array. If it actually returns
    # an empty list, something went wrong and tells caller frame is invalid
    if needed > len(samples):
        return []

    mag = np.abs(samples)
    bits = []

    for n in range(data_bits):
        #Calculate the start index of the current bit in the samples array
        #Each bit is represented by samples_per_bit samples, so to find the start of the nth bit,
        # multiply n by samples_per_bit and add it to data_start
        start = data_start + n * samples_per_bit
        #Define the two sample indices within the bit period to compare
        #Early sample represent early pulse
        #Late sample represent late pulse
        i0 = start
        i1 = start + 1

        if i1 >= len(mag):
            break

        chip0 = mag[i0]
        chip1 = mag[i1]
        
        #Essentially if pulse energy is higher at early samples, bit is 1
        #If pulse energy is higher at late samples, bit is 0
        # early pulse means 1, late pulse means 0
        bits.append(1 if chip0 > chip1 else 0)

    return bits

