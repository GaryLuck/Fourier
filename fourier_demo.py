"""Fourier Transform demonstration with ASCII terminal graphs."""

import math
import numpy as np


def generate_sine(num_samples, periods=2):
    """Generate a sine wave."""
    return [math.sin(2 * math.pi * periods * i / num_samples) for i in range(num_samples)]


def generate_square(num_samples, periods=2):
    """Generate a square wave."""
    samples = []
    for i in range(num_samples):
        phase = (periods * i / num_samples) % 1.0
        samples.append(1.0 if phase < 0.5 else -1.0)
    return samples


def generate_sawtooth(num_samples, periods=2):
    """Generate a sawtooth wave."""
    samples = []
    for i in range(num_samples):
        phase = (periods * i / num_samples) % 1.0
        samples.append(2.0 * phase - 1.0)
    return samples


def draw_ascii_graph(values, title, width=70, height=15):
    """Draw an ASCII graph that scrolls vertically in the terminal."""
    print(f"\n  === {title} ===\n")

    v_min = min(values)
    v_max = max(values)
    # Avoid division by zero for flat signals
    v_range = v_max - v_min if v_max != v_min else 1.0

    # Resample values to fit the desired width
    resampled = []
    for col in range(width):
        idx = int(col * len(values) / width)
        idx = min(idx, len(values) - 1)
        resampled.append(values[idx])

    # Build the graph row by row from top to bottom
    for row in range(height):
        # Map row to value: top row = v_max, bottom row = v_min
        threshold = v_max - (row / (height - 1)) * v_range

        # Y-axis label
        if row == 0:
            label = f"{v_max:>7.2f} |"
        elif row == height - 1:
            label = f"{v_min:>7.2f} |"
        elif row == height // 2:
            mid = (v_max + v_min) / 2
            label = f"{mid:>7.2f} |"
        else:
            label = "        |"

        line = []
        for col in range(width):
            val = resampled[col]
            # Normalize to row space
            val_row = (v_max - val) / v_range * (height - 1)
            if abs(val_row - row) < 0.5:
                line.append("*")
            else:
                line.append(" ")

        print(label + "".join(line))

    # X-axis
    print("        +" + "-" * width)


def compute_fft_magnitudes(signal):
    """Compute FFT and return magnitude spectrum (positive frequencies only)."""
    n = len(signal)
    fft_result = np.fft.fft(signal)
    magnitudes = np.abs(fft_result[:n // 2]) / n
    # Double the non-DC components to account for symmetric spectrum
    magnitudes[1:] *= 2
    return magnitudes.tolist()


def main():
    num_samples = 128
    periods = 4

    while True:
        print("\n" + "=" * 50)
        print("   FOURIER TRANSFORM DEMONSTRATION")
        print("=" * 50)
        print("\n  Select a waveform:\n")
        print("    1. Sine wave")
        print("    2. Square wave")
        print("    3. Sawtooth wave")
        print("    q. Quit")

        choice = input("\n  Enter choice (1/2/3/q): ").strip().lower()

        if choice == "q":
            print("\n  Goodbye!\n")
            break

        if choice == "1":
            name = "Sine Wave"
            signal = generate_sine(num_samples, periods)
        elif choice == "2":
            name = "Square Wave"
            signal = generate_square(num_samples, periods)
        elif choice == "3":
            name = "Sawtooth Wave"
            signal = generate_sawtooth(num_samples, periods)
        else:
            print("  Invalid choice. Try again.")
            continue

        # Draw time domain
        draw_ascii_graph(signal, f"Time Domain - {name}")

        # Compute and draw frequency domain
        magnitudes = compute_fft_magnitudes(signal)
        # Show only the first 32 bins for readability
        display_bins = magnitudes[:32]
        draw_ascii_graph(display_bins, f"Frequency Domain - {name} (magnitude)")

        print(f"\n  Peak frequency bin: {magnitudes.index(max(magnitudes[1:]))} "
              f"(expect ~{periods})")


if __name__ == "__main__":
    main()
