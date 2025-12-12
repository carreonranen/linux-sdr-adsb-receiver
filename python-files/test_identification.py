from decode_all_frames import decode_all_frames
from payload_decoder import summarize_payload
from decode_identification import decode_callsign

# Helper function to conditionally decode callsign
def main():

    frames = decode_all_frames()
    print(f"Total decoded frames: {len(frames)}")

    # Look for DF 17 identification frames
    for f in frames:
        # ADS B extended squitter is DF 17
        if f["df"] != 17:
            continue
            # only decode identification messages
        info = summarize_payload(f["rawM"])
        tc = info["tc"]

        # type codes 1 to 4 carry identification
        if not (1 <= tc <= 4):
            continue
            # decode callsign
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

