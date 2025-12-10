# decode_all_frames.py

from load_capture import load_iq_file
from preamble_detection import findPreambleIndices
from bit_extraction import samples_to_bits
from frame_parser import parseFrame
from constants import sample_rate
from payload_decoder import summarize_payload


def decode_all_frames():
    path = "../captures/adsb_200k.iq"
    print(f"Loading samples from {path}...")
    samples = load_iq_file(path)
    print(f"Loaded {len(samples)} samples.")

    pre_indices = findPreambleIndices(samples, sample_rate)
    print(f"Found {len(pre_indices)} preamble candidates.")

    decoded = []

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

    print(f"Successfully decoded {len(decoded)} frames.")
    return decoded


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


if __name__ == "__main__":
    main()

