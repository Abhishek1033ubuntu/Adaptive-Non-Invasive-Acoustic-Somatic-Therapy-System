```python
import tkinter as tk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import csv
import random
import os
from datetime import datetime

# Set modern medical dark theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MedicalMasterSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Acoustic Somatic Therapy - Master Clinical Interface")
        self.geometry("1200x700")
        
        # System Variables & Data Logging
        self.is_running = False
        self.after_id = None  
        self.stress_history = list(np.ones(50) * 0.95) 
        self.session_data_log = [] # Stores live data for the CSV report
        self.current_frequency = 75.0 # Starting crisis frequency
        
        # Protocol safety clean exit handler
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # --- UI LAYOUT MATRIX ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)
        
        # LEFT CONTROL PANEL
        self.control_panel = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.control_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.lbl_title = ctk.CTkLabel(self.control_panel, text="CLINICAL SYSTEM", font=ctk.CTkFont(size=20, weight="bold"))
        self.lbl_title.pack(pady=20, padx=10)
        
        self.lbl_dropdown = ctk.CTkLabel(self.control_panel, text="Select Therapeutic Prescription:")
        self.lbl_dropdown.pack(pady=5)
        self.regimen_menu = ctk.CTkOptionMenu(self.control_panel, values=["Vagal Tone (Discovered Sqrt(2))", "Micro-Vascular Flow"])
        self.regimen_menu.pack(pady=10)
        
        self.btn_start = ctk.CTkButton(self.control_panel, text="Initialize Session", command=self.toggle_session, fg_color="green", hover_color="darkgreen")
        self.btn_start.pack(pady=20, padx=20)
        
        # Safety Alert Indicator Box
        self.safety_alert = ctk.CTkFrame(self.control_panel, height=80, fg_color="#2B2B2B")
        self.safety_alert.pack(pady=30, padx=20, fill="x")
        self.lbl_safety = ctk.CTkLabel(self.safety_alert, text="SYSTEM READY\nDATA LOGGER: STANDBY", font=ctk.CTkFont(size=12))
        self.lbl_safety.pack(pady=20)
        
        # RIGHT MONITOR PANEL
        self.monitor_panel = ctk.CTkFrame(self)
        self.monitor_panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # Embed Matplotlib Live Plotting Window
        self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor="#2B2B2B")
        self.ax.set_facecolor("#1C1C1C")
        self.ax.tick_params(colors='white')
        self.ax.grid(True, color="#444444")
        self.ax.set_title("Live Patient Biometric Telemetry (Simulated Biological Noise)", color="white")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.monitor_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=20)
        
    def toggle_session(self):
        if not self.is_running:
            self.is_running = True
            self.session_data_log = [["Timestamp", "Applied_Frequency_Hz", "Relative_Stress_Level"]]
            self.current_frequency = 75.0
            
            self.btn_start.configure(text="Terminate & Export Report", fg_color="red", hover_color="darkred")
            self.lbl_safety.configure(text="⚠️ CRISIS MODE ACTIVE\nRECORDING BIOMETRICS...", fg_color="darkred")
            self.update_live_loop()
        else:
            self.is_running = False
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
                
            self.export_medical_report()
            
            self.btn_start.configure(text="Initialize Session", fg_color="green", hover_color="darkgreen")
            self.lbl_safety.configure(text="SESSION LOGGED.\nREPORT SAVED TO SCRIPT DIR.", fg_color="#2B2B2B")

    def update_live_loop(self):
        if self.is_running:
            self.stress_history.pop(0)
            
            # --- VIRTUAL PATIENT SIMULATOR ---
            current_lowest = self.stress_history[-1]
            biological_noise = random.uniform(-0.02, 0.04)
            next_val = max(0.05, min(1.0, current_lowest - 0.015 + biological_noise))
            self.stress_history.append(next_val)
            
            # Down-modulate frequency for report
            self.current_frequency = max(40.0, self.current_frequency - 0.5)
            
            # Log timestamped data
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            self.session_data_log.append([timestamp, round(self.current_frequency, 2), round(next_val, 3)])
            
            try:
                self.ax.clear()
                self.ax.set_facecolor("#1C1C1C")
                self.ax.grid(True, color="#444444")
                self.ax.plot(self.stress_history, color="cyan", lw=2.5, label="Simulated HRV Stress Index")
                self.ax.set_ylim(-0.05, 1.1)
                self.ax.tick_params(colors='white')
                self.ax.legend(loc="upper right")
                self.canvas.draw()
            except Exception:
                return 
            
            self.after_id = self.after(200, self.update_live_loop)

    def export_medical_report(self):
        if len(self.session_data_log) > 1:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filename = datetime.now().strftime("Session_Report_%Y%m%d_%H%M%S.csv")
            filepath = os.path.join(script_dir, filename)
            
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.session_data_log)
            print(f"Medical Report Exported Successfully to: {filepath}")

    def on_closing(self):
        self.is_running = False
        if self.after_id:
            self.after_cancel(self.after_id)
        if len(self.session_data_log) > 1:
            self.export_medical_report()
        plt.close('all') 
        self.destroy()

if __name__ == "__main__":
    app = MedicalMasterSystem()
    app.mainloop()
