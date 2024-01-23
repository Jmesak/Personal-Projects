# Resource Monitor Project

ResourceMonitor.exe is present in the dist folder

**Function:**
A basic and low-resource intensive GUI that displays real-time CPU, GPU, and RAM usage as graphical data - similar to the Windows Resource Monitor and Task Manager.

**Notable trouble-shooting/learning moments included:**
- Learning additional tkinter utility, notably FigureCanvasTkAgg from matplotlib.backends.backend_tkagg
- Pulling cpu and RAM usage data via psutil, and gpu usage with pynvml (I have an nvidia gpu, idk how this would fair with other gpus)
- Converting psutil data into graphs with matplot.lib
- Verifying results with Windows utilities

**Additions for Future Versions**
- Making the GUI and graphs look nicer
- Keep default domain and range, but maybe make it adjustable in GUI (graph data time limit and option to switch from static 0-100 y-axis to a dynamic one)
- Display CPU, RAM, and GPU model; as well as showing threads/cores, ram amount, gpu vram, etc.

```python
#Jonathan Mesak
#01/23/2024

import psutil
import tkinter as tk #Using instead of "from tkinter import *" like in password_gen.py because multiple modules are being used
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pynvml

def update_labels():
    #Update CPU usage
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")

    #Update GPU usage
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    gpu_info = pynvml.nvmlDeviceGetUtilizationRates(handle)
    gpu_percent = gpu_info.gpu
    gpu_label.config(text=f"GPU Usage: {gpu_percent}%")

    #Update memory usage
    memory_percent = psutil.virtual_memory().percent
    memory_label.config(text=f"Memory Usage: {memory_percent}%")

    #Update graph data
    cpu_data.append(cpu_percent)
    gpu_data.append(gpu_percent)
    memory_data.append(memory_percent)

    #Limit the graph data to the last 60 seconds
    if len(cpu_data) > 600:
        cpu_data.pop(0)
        gpu_data.pop(0)
        memory_data.pop(0)

    #Update the graphs
    ax1.clear()
    ax1.plot(cpu_data, label="CPU", color = "red")
    ax1.set_xlabel("Time (seconds)")
    ax1.set_ylabel("Usage (%)")
    ax1.set_title("CPU")
    ax1.set_ylim(0, 100)

    ax2.clear()
    ax2.plot(gpu_data, label="GPU", color = "blue")
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Usage (%)")
    ax2.set_title("GPU")
    ax2.set_ylim(0, 100)

    ax3.clear()
    ax3.plot(memory_data, label="Memory", color = "green")
    ax3.set_xlabel("Time (seconds)")
    ax3.set_ylabel("Usage (%)")
    ax3.set_title("Memory")
    ax3.set_ylim(0, 100)

    canvas.draw()

    root.after(100, update_labels)

root = tk.Tk()
root.title("Resource Monitor")

cpu_label = tk.Label(root, text="CPU Usage: -")
cpu_label.pack()

gpu_label = tk.Label(root, text="GPU Usage: -")
gpu_label.pack()

memory_label = tk.Label(root, text="Memory Usage: -")
memory_label.pack()

root.wm_attributes('-toolwindow', 'True') #Removes tkinter favicon from top bar

# Create the graphs
fig = plt.Figure(figsize=(6, 8), dpi=100)
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

#Spacing between graphs because of label overlap
fig.subplots_adjust(hspace=0.5, wspace=0.5)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

canvas.get_tk_widget().pack(padx=10, pady=10)

# Initialize graph data
cpu_data = []
gpu_data = []
memory_data = []

update_labels()

root.mainloop()
```
