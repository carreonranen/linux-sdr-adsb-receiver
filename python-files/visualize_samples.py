import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless mode
import matplotlib.pyplot as plt  # noqa: E402

from load_capture import load_iq_file


def main() -> None:
    path = "../captures/adsb_200k.iq"
    samples = load_iq_file(path)

    mag = np.abs(samples)

    plt.figure(figsize=(12, 4))
    plt.plot(mag, linewidth=0.7)
    plt.title("ADS B IQ Sample Magnitude")
    plt.xlabel("Sample index")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()

    out_path = "../captures/adsb_magnitude_plot.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved plot to {out_path}")


if __name__ == "__main__":
    main()

