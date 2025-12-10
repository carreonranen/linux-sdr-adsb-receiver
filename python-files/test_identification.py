from decode_all_frames import decode_all_frames
from payload_decoder import summarize_payload
from decode_identification import decode_callsign


def main() -> None:
    frames = decode_all_frames()
    print(f"Total decoded frames: {len(frames)}")

    for f in frames:
        # ADS B extended squitter is DF 17
        if f["df"] != 17:
            continue

        info = summarize_payload(f["rawM"])
        tc = info["tc"]

        # type codes 1 to 4 carry identification
        if not (1 <= tc <= 4):
            continue

        icao = f["icao"]
        callsign = decode_callsign(f["rawM"])

        print("Found aircraft identification frame:")
        print("  ICAO     :", icao)
        print("  DF       :", f["df"])
        print("  TypeCode :", tc)
        print("  Callsign :", callsign)
        break
    else:
        print("No DF 17 identification frames found.")


if __name__ == "__main__":
    main()

