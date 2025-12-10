# log_frames.py

import csv
from typing import Optional

from decode_all_frames import decode_all_frames
from payload_decoder import summarize_payload
from decode_identification import decode_callsign


def maybe_decode_callsign(df: int, category: str, rawM: int) -> Optional[str]:
    # only decode callsign for DF 17 and identification messages
    if df != 17:
        return None
    if category != "Aircraft Identification":
        return None
    return decode_callsign(rawM)


def main():
    frames = decode_all_frames()
    print(f"Total decoded frames: {len(frames)}")

    csv_path = "../docs/frames_log.csv"

    with open(csv_path, mode="w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(
            [
                "index",
                "sample_index",
                "df",
                "ca",
                "icao",
                "tc",
                "category",
                "rawM",
                "crc",
                "callsign",
            ]
        )

        for idx, frame in enumerate(frames):
            df = frame["df"]
            ca = frame["ca"]
            icao = frame["icao"]
            rawM = frame["rawM"]
            crc = frame["rawCRC"]
            sample_index = frame["sample_index"]

            payload_info = summarize_payload(rawM)
            tc = payload_info["tc"]
            category = payload_info["category"]

            callsign = maybe_decode_callsign(df, category, rawM)

            writer.writerow(
                [
                    idx,
                    sample_index,
                    df,
                    ca,
                    icao,
                    tc,
                    category,
                    rawM,
                    crc,
                    callsign or "",
                ]
            )

    print(f"Wrote frame log to {csv_path}")


if __name__ == "__main__":
    main()

