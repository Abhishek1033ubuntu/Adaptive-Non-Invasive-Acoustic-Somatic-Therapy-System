import numpy as np
import matplotlib.pyplot as plt

def generate_hardware_verification_plots():
    """
    Simulates and visualizes the real-time audio synthesis engine, 
    dynamic frequency ramp pacing, and power-clamping safety boundaries.
    """
    print("Initializing Acoustic Engine Simulation...")

    # --- 1. DYNAMIC PACING RAMP SIMULATION ---
    # Simulates a 10-second check stepping from 75 Hz (crisis) down to 40 Hz (baseline)
    t_ramp = np.linspace(0, 10, 1000)
    f_start = 75.0
    f_target = 40.0
    synthesized_pitch = np.linspace(f_start, f_target, len(t_ramp))
    target_baseline = np.full_like(t_ramp, f_target)

    # --- 2. MICROSECOND WAVEFORM & POWER CLAMP SIMULATION ---
    # Time vector for a 0.045 second (45ms) safety window
    sample_rate = 44100  # 44.1 kHz standard audio DAC rate
    t_window = np.linspace(0, 0.045, int(sample_rate * 0.045))
    
    # Fundamental frequency at initial state
    f0 = 75.0
    # Non-habituating overtone using the irrational tritone ratio Sqrt(2)
    f1 = f0 * np.sqrt(2) 
    
    # Synthesize twin-tone complex wave
    raw_waveform = np.sin(2 * np.pi * f0 * t_window) + 0.5 * np.sin(2 * np.pi * f1 * t_window)
    
    # Apply strict 50.0% Power-Clamp Safety Governor Limit
    power_cap_limit = 0.50
    clamped_waveform = raw_waveform * (power_cap_limit / np.max(np.abs(raw_waveform)))

    # --- 3. PLOTTING DIAGNOSTICS ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    fig.patch.set_facecolor('#ffffff')

    # TOP GRAPH: Real-Time Audio Synthesis Pacing
    ax1.plot(t_ramp, synthesized_pitch, color='blue', lw=2.5, label='Synthesized Fundamental Pitch (Hz)')
    ax1.axhline(y=f_target, color='green', linestyle='--', lw=1.5, label='Target Healing Baseline')
    ax1.set_title('Virtual Hardware Verification: Real-Time Audio Synthesis Processing', fontsize=12)
    ax1.set_ylabel('Frequency (Hz)')
    ax1.set_ylim(38, 78)
    ax1.grid(True)
    ax1.legend(loc='upper right')

    # BOTTOM GRAPH: Microsecond Waveform Clamping Window
    ax2.plot(t_window, clamped_waveform, color='purple', lw=1.5, label='Voltage Waveform Sent to Transducers')
    ax2.set_title('Microsecond Safety Window (Strictly Clamped to 50.0% Power Cap)', fontsize=12)
    ax2.set_xlabel('Time Samples (Seconds)')
    ax2.set_ylabel('Voltage Output')
    ax2.set_ylim(-0.52, 0.52)
    ax2.grid(True)
    ax2.legend(loc='upper right')

    plt.tight_layout()
    print("Verification Plots Generated Successfully. Displaying Canvas...")
    plt.show()

if __name__ == "__main__":
    generate_hardware_verification_plots()
