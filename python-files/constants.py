# constants.py

#Thisfile defines  all global and constant parameters used across the ADS-B receiver project



# SDR radio settings
#ADS B aircraft transponders broadcast at 1090 MHz. Internationally standardized frequency
#So all aircrtaft and receivers know where to communicate with one another
centr_freq = 1_090_000_000  # Hz
#Defines how many samples per second the SDR captures. Higher sample rates provide better resolution
sample_rate = 2_000_000     # samples per second
#Gain setting for the SDR. "auto" lets the SDR choose optimal gain
gain = "auto"

# ADS-B parameters
#ADS B uses a fixed rate of 1 Mbps and is defined by ICAO standards. Any other number
# would not be compatible with existing ADS-B systems and receivers
bit_rate = 1_000_000
#Calculates the duration of each bit in seconds
bit_period = 1.0 / bit_rate
#ADS-B preamble duration is 8 microseconds(globally known)
preamble = 8          # in microseconds
#Number of data bits in an ADS-B message(payload excluding preamble)
data_bits = 112
#Total number of bits in an ADS-B frame including preamble.
#This is for validation purposes later implemented in the decoder, not used atm
frame_bits = data_bits

