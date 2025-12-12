import numpy as np
from load_capture import load_iq_file
from preamble_detection import findPreambleIndices
from bit_extraction import samples_to_bits
from frame_parser import parseFrame
from constants import sample_rate

# log_frames.py
def main():
    # Load IQ samples from a .iq file
    path = "../captures/adsb_200k.iq"
    print(f"Loading samples from {path}...")
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} samples.")

    # Detect preamble indices in the samples
    pre_indices = findPreambleIndices(samples, sample_rate)
    print(f"Found {len(pre_indices)} preamble candidates.")

    # Try decoding a few candidates
    if not pre_indices:
        print("No preamble candidates found.")
        return
    
    # just try a few
    for idx in pre_indices[:10]:
        print(f"\nTrying candidate at sample {idx}")
        bits = samples_to_bits(samples, idx)
        print(f"Extracted {len(bits)} bits")

        if len(bits) != 112:
            print("Not a full frame, skipping")
            continue

        try:
            frame = parseFrame(bits)
        except Exception as e:
            print("parseFrame failed:", e)
            continue
            # ignore broken frames

    # If this function gets to  got here,  have a decoded frame
        print("Decoded frame:")
        print("  df   :", frame["df"])
        print("  ca   :", frame["ca"])
        print("  icao :", frame["icao"])
        print("  rawM :", frame["rawM"])
        print("  crc  :", frame["rawCRC"])
        break


if __name__ == "__main__":
    main()

