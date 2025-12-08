Linux-Based SDR Wireless Communications System (ADS-B Receiver)

Built with Raspberry Pi 4, RTL-SDR Blog V4, Python, and Linux

This project is a complete wireless communications system that receives, demodulates, and decodes real-world aircraft ADS-B signals at 1090 MHz.
It demonstrates RF engineering fundamentals, Linux systems work, SDR signal processing, protocol decoding, and end-to-end hardware/software integration.

**Skills Demonstrated**
* Linux system configuration
* Python scripting + tooling
* Software Defined Radio (RTL-SDR Blog V4)
* Signal processing (I/Q data, FFT, magnitude analysis)
* Pulse-Position Modulation (PPM) decoding
* Bit-level protocol parsing (Mode S / ADS-B)
* Hardware integration (filters, antennas, Raspberry Pi)
* Data engineering + CSV logging
* Visualization + system analysis

**Project Overview**
Uses a RAS PI 4 and RTL-SDR Blog V4, the system will:
1) Capture raw IQ samples at 2ms 
2) Detects ADS-B preambles
3) Demodulates PPM bits from Preamble
4) Decodes DF(Downlink Format), CA(Transponder Capability), ICAO(International Civilization Avitation Organization), Type Code, and the CRC(Cyclic Redundancy Check)
5) Extracts aircraft identification messages (the callsigns)
6) Logs all decoded frames into CSV
7) Use Matplotlib to Visualize message categories

**System Features**
* [x] Real-time IQ capture
* [x] PPM demodulation from I/Q Samples
* [x] Automatic Preamble Detection
* [x] Bit slicing + 112-bit ADS-B frame extraction
Decoding of:
* [x]CA (Capability)
* [x]ICAO aircraft address
* [x]Type code & Category
* [x]Aircraft callsign
* []Aircraft Elevation Information (Work in progress)

**Features**
* Real time ADS-b signal reception
* Python-based custom decoder
* PPM demodulation + CRC validation
* Raw IQ logging
* Aircraft visualization on map
* Runs on Raspberry Pi 4 (low power embedded Linux)

**Repository Structure**
```bash
linux-sdr-adsb-receiver/
│
├── README.md
│
├── docs/
│   ├── week1_theory.md
│   ├── week2_demodulation.md
│   ├── week3_decoding.md
│   ├── week4_results.md
│   ├── frames_log.csv
│   └── images/
│       ├── magnitude_plot.png
│       └── type_code_histogram.png
│
├── captures/
│   └── adsb_200k.iq
│
├── python/
│   ├── capture_samples.py
│   ├── decode_all_frames.py
│   ├── decode_identification.py
│   ├── payload_decoder.py
│   ├── preamble_detection.py
│   ├── samples_to_bits.py
│   ├── test_identification.py
│   ├── visualize_type_codes.py
│   └── log_frames.py
│
└── hardware/
    ├── antenna_setup.jpg
    └── filter_and_sdr.jpg

```


**Demo Images**
Magnitude plot of raw IQ data
<img width="1200" height="400" alt="adsb_magnitude_plot" src="https://github.com/user-attachments/assets/b69f0023-4258-4e67-a8ba-d5141ffeb913" />

Detected preambles
<img width="1614" height="310" alt="2025-12-08_13-56" src="https://github.com/user-attachments/assets/3669ce77-b6be-45db-b63c-c01a074a4a35" />

Terminal output of decoded ADS-B frames
<img width="1612" height="532" alt="2025-12-08_13-57" src="https://github.com/user-attachments/assets/c300bb94-b1b8-4514-9394-01a595efba41" />

Histogram of ADS-B message categories
<img width="1500" height="750" alt="type_code_histogram(1)" src="https://github.com/user-attachments/assets/b3f329e5-d79a-4738-9435-c25a32dc464d" />

**UNKOWN is work in progress and is most likely altitude**


Hardware (antenna, filter, RTL-SDR, Raspberry Pi)

**How to Run**

**Background / Theory**

**Author**:
Ranen Carreon 
