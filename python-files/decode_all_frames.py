# decode_all_frames.py



#Purpose of this script:
#1) Open/Acquire IQ samples
#2) Detect preambles in the samples
#3) Extract bits from the samples based on preamble locations (Demodulate PPM to produce 112 bits)
#4) Parse the extracted bits into ADS-B frames
#5) Decode the payload of each frame to get human-readable info
#6) Print a summary of the decoded frames

from load_capture import load_iq_file
from preamble_detection import findPreambleIndices
from bit_extraction import samples_to_bits
from frame_parser import parseFrame
from constants import sample_rate
from payload_decoder import summarize_payload


def decode_all_frames():
    #Load IQ samples from a .iq file
    path = "../captures/adsb_200k.iq"
    print(f"Loading samples from {path}...")
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} samples.")

    #Detect preamble indices in the samples
    pre_indices = findPreambleIndices(samples, sample_rate)
    print(f"Found {len(pre_indices)} preamble candidates.")

    #Extract bits and parse frames
    decoded = []
    #For each detected preamble index, extract bits and parse frame
    for idx in pre_indices:
        bits = samples_to_bits(samples, idx)

        # expect a full 112 bit frame
        if len(bits) != 112:
            continue

        try:
            frame = parseFrame(bits)
        except Exception:
            # ignore broken frames
            continue

        frame["sample_index"] = idx
        decoded.append(frame)


    # Summary of results
    print(f"Successfully decoded {len(decoded)} frames.")
    return decoded

    # return list of decoded frames
def main():
    frames = decode_all_frames()

    max_to_show = 10
    for i, f in enumerate(frames[:max_to_show]):
        payload_info = summarize_payload(f["rawM"])

        print(
            f"[{i}] idx={f['sample_index']}  "
            f"df={f['df']}  ca={f['ca']}  icao={f['icao']}  "
            f"tc={payload_info['tc']}  type={payload_info['category']}  "
            f"rawM={f['rawM']}  crc={f['rawCRC']}"
        )

# Run the main function if this script is executed directly
#This is a safeguard to ensure main() runs only when this file is run as a script,
# not when imported as a module in another script.
if __name__ == "__main__":
    main()

