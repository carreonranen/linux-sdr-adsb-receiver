**Linux Based SDR Wireless Communications System (ADS-B Receiver)**

Built with Raspberry Pi 4, RTL-SDR Blog V4, Python, and Linux

**Skills Demonstrated**
* Linux
* Python
* Signal processing
* SDR
* Hardware integration
* Embedded systems
* Data engineering
* RF engineering fundamentals

**A complete wireless communications project demonstrating:**
* Software Defined Radio
* Linux system configuration
* Signal processing
* Modulation decoding (PPM)
* Hardware–software integration
* Real time aircraft tracking

**System Architecture**


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
├── docs/
│   ├── week1_setup.md
│   ├── week2_decoder.md
│   ├── week3_integration.md
│   ├── week4_results.md
│   └── block_diagram.png
│
├── hardware/
│   ├── bill_of_materials.md
│   ├── antenna_setup.jpg
│   └── wiring_diagram.png
│
├── python/
│   ├── samples/
│   │   └── out.bin
│   ├── test_sdr.py
│   ├── decoder.py
│   ├── preamble_detection.py
│   ├── bit_extraction.py
│   └── message_parser.py
│
├── data/
│   ├── aircraft_log.csv
│   ├── raw_iq/
│   │   └── sample1.bin
│   └── plots/
├── End

```

**Demo Images**
Screenshots of:
* dump1090
* your antenna setup
* your Python decoder output
* map visualization

**How to Run**

**Background / Theory**

**Author**:
Ranen Carreon 
