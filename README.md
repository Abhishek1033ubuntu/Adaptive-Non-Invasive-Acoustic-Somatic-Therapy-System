# Adaptive Non-Invasive Acoustic Somatic Therapy System
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21708728.svg)](https://doi.org/10.5281/zenodo.21708728)  ![Status](https://img.shields.io/badge/Status-Research_POC-orange) ![Type](https://img.shields.io/badge/Type-Simulation_Model-blue)

**Version:** 1.0 (Clinical Prototype Phase)  
**Status:** Software Verified & Simulated  

## Overview
This repository contains the software suite, mathematical framework, and hardware specifications for an adaptive acoustic somatic therapy device designed to down-regulate acute physiological stress and stimulate vagal tone. 

The system synthesizes dynamic, phase-continuous mechanical waves in real time using a non-habituating harmonic matrix ($f_1 = f_0 \times \sqrt{2}$) and features an automated biometric safety governor to prevent mechanical over-excitation during acute hyperarousal events.

---

## Repository Contents
* `app.py`: Modern CustomTkinter clinical dashboard with virtual biological noise simulation and automated CSV report exporter.
* `system_emulator.py`: Desktop verification script for testing real-time audio synthesis curves and power-clamping math.

---

## System Hardware Specification

### Core Component Array
* **Microprocessor:** Teensy 4.1 ($600\text{ MHz}$ ARM Cortex)
* **Biometric Sensor:** MAX30102 High-Sensitivity PPG Oximeter (I2C)
* **DAC:** NXP UDA1334A I2S Stereo Decoder Breakout Board
* **Amplifier Stage:** PAM8403 Class-D Mini Amplifier ($5\text{V}$)
* **Transducers:** 2x Dayton Audio TT25-8 Puck Tactile Mini Bass Shakers ($8\text{ Ohm}$)

### Pin Configuration Matrix

| Source Component | Source Pin | Destination Component | Destination Pin | Protocol / Function |
| :--- | :--- | :--- | :--- | :--- |
| **Teensy 4.1** | `3.3V` | **MAX30102 PPG** | `VCC` | Logic Power |
| **Teensy 4.1** | `GND` | **MAX30102 PPG** | `GND` | Ground Reference |
| **Teensy 4.1** | `Pin 18` | **MAX30102 PPG** | `SDA` | I2C Serial Data |
| **Teensy 4.1** | `Pin 19` | **MAX30102 PPG** | `SCL` | I2C Serial Clock |
| **Teensy 4.1** | `Pin 2` | **MAX30102 PPG** | `INT` | Event Interrupt |
| **Teensy 4.1** | `5V` | **UDA1334A DAC** | `VIN` | Board Power |
| **Teensy 4.1** | `GND` | **UDA1334A DAC** | `GND` | Ground Reference |
| **Teensy 4.1** | `Pin 7` | **UDA1334A DAC** | `DIN` | I2S Audio Data |
| **Teensy 4.1** | `Pin 20` | **UDA1334A DAC** | `WSEL` | I2S Word Select (LRCLK) |
| **Teensy 4.1** | `Pin 21` | **UDA1334A DAC** | `BCLK` | I2S Bit Clock |

### Analog Signal Path Safety Sequence
[UDA1334A DAC Analog L/R Out]
│
▼
[10k Ohm Linear Potentiometer] ─── (Hardware Gain Ceiling)
│
▼
[Latching Mushroom E-STOP Switch] ── (Mechanical Hardware Interrupt)
│
▼
[PAM8403 Class-D Amplifier Inputs]
│
▼
[Dayton Audio TT25-8 Tactile Shakers]

## Software Quickstart

### Prerequisites
* Python 3.10+
* Windows, macOS, or Linux

### Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/Abhishek1033ubuntu/Adaptive-Non-Invasive-Acoustic-Somatic-Therapy-System.git](https://github.com/Abhishek1033ubuntu/Adaptive-Non-Invasive-Acoustic-Somatic-Therapy-System.git)
   cd Abhishek1033ubuntu
Install required dependencies:

Bash
pip install customtkinter matplotlib numpy scipy

Run the Clinical Control Interface:

Bash
python app.py

How to Run It:
In your terminal/Command Prompt, simply run:
python system_emulator.py
