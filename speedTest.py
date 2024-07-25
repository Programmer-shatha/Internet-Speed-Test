import tkinter as tk
from tkinter import ttk
from speedtest import Speedtest
import threading

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        self.root.geometry("500x400")
        self.root.configure(bg="#282c34")
        
        self.label = tk.Label(root, text="Internet Speed Test", font=("Helvetica", 20, "bold"), bg="#282c34", fg="#61dafb")
        self.label.pack(pady=20)
        
        self.download_label = tk.Label(root, text="Download Speed: N/A", font=("Helvetica", 14), bg="#282c34", fg="white")
        self.download_label.pack(pady=10)
        
        self.upload_label = tk.Label(root, text="Upload Speed: N/A", font=("Helvetica", 14), bg="#282c34", fg="white")
        self.upload_label.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Test", font=("Helvetica", 12, "bold"), bg="#61dafb", fg="white", command=self.start_test)
        self.start_button.pack(pady=20)
        
        self.progress = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=300)
        self.progress.pack(pady=20)
        
    def start_test(self):
        self.progress.start(10)
        self.start_button.config(state=tk.DISABLED)
        self.download_label.config(text="Download Speed: Testing...")
        self.upload_label.config(text="Upload Speed: Testing...")
        
        threading.Thread(target=self.run_speed_test).start()
        
    def run_speed_test(self):
        wifi = Speedtest()
        
        download = wifi.download()
        upload = wifi.upload()
        
        download_speed = download / 1024 / 1024
        upload_speed = upload / 1024 / 1024
        
        self.update_results(download_speed, upload_speed)
        
    def update_results(self, download_speed, upload_speed):
        self.download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        self.upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
        self.progress.stop()
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TProgressbar", foreground='#61dafb', background='#61dafb')
    
    root.mainloop()