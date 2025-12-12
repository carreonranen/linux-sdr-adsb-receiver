import numpy as np
import matplotlib
# visualization_samples.py


matplotlib.use("Agg")  # 
import matplotlib.pyplot as plt  #

from load_capture import load_iq_file

# Visualize the magnitude of IQ samples from an ADS-B capture file
def main():
    # Load samples
    path = "../captures/adsb_200k.iq"
    samples = load_iq_file(path)
    # Compute magnitude
    mag = np.abs(samples)
    # Plot magnitude
    plt.figure(figsize=(12, 4))
    plt.plot(mag, linewidth=0.7)
    plt.title("ADS B IQ Sample Magnitude")
    plt.xlabel("Sample index")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    
    # Save plot
    out_path = "../captures/adsb_magnitude_plot.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved plot to {out_path}")


if __name__ == "__main__":
    main()

