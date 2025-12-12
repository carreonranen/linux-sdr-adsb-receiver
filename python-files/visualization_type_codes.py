import csv
from collections import Counter
import matplotlib.pyplot as plt

CSV_PATH = "../docs/frames_log.csv"

# Load frame categories from CSV file
def load_categories(csv_path: str):
    cats = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = (row.get("category") or "").strip()
            if cat:
                cats.append(cat)
    return cats

# Plot histogram of frame type codes
def plot_histogram() -> None:
    cats = load_categories(CSV_PATH)
    print(f"Loaded {len(cats)} frame categories.")
    # Count occurrences of each category
    counts = Counter(cats)
    
    print("Category counts:")
    for cat, cnt in counts.items():
        print(f"  {cat}: {cnt}")

    labels = list(counts.keys())
    values = [counts[l] for l in labels]
    # Create bar chart
    plt.figure(figsize=(9, 4))
    bars = plt.bar(labels, values)
    #
    plt.title("ADS B Message Type Distribution")
    plt.xlabel("Message Category")
    plt.ylabel("Count")
    plt.xticks(rotation=25, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    if values:
        max_val = max(values)
    else:
        max_val = 0

    for bar in bars:
        h = bar.get_height()
        if h > 0:
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                h + max_val * 0.02,
                str(h),
                ha="center",
                va="bottom",
                fontsize=9,
            )

    plt.tight_layout()
    out_path = "../docs/images/type_code_histogram.png"
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved histogram to {out_path}")


if __name__ == "__main__":
    plot_histogram()

