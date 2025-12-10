# constants.py

# SDR radio settings
centr_freq = 1_090_000_000  # Hz
sample_rate = 2_000_000     # samples per second
gain = "auto"

# ADS-B parameters
bit_rate = 1_000_000
bit_period = 1.0 / bit_rate
preamble = 8          # in microseconds
data_bits = 112
frame_bits = data_bits

