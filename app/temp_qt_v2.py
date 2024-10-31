import os
import glob
import time
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.colors as mcolors
import matplotlib.cm as cm

class TemperatureSensor:
    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read_temp_raw(self):
        with open(self.device_file, 'r') as f:
            lines = f.readlines()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = int(temp_string) / 1000
            return temp_c

class TemperaturePlotWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(10, 9), dpi=80)
        self.ax = self.fig.add_subplot(111)
        
        self.sensor = TemperatureSensor()

        self.min_temp, self.max_temp = 0, 100
        self.norm = mcolors.Normalize(vmin=self.min_temp, vmax=self.max_temp)
        self.cmap = cm.get_cmap('viridis')

        self.sm = cm.ScalarMappable(cmap=self.cmap, norm=self.norm)
        self.sm.set_array([])
        self.cbar = self.fig.colorbar(self.sm, ax=self.ax, orientation='vertical')

        super(TemperaturePlotWidget, self).__init__(self.fig)
        self.setParent(parent)

        self.temps = []
        self.max_len = 50

        self.update_plot()

    def resizeEvent(self, event):
        self.fig.set_size_inches(self.width() / self.fig.get_dpi(), self.height() / self.fig.get_dpi())
        super(TemperaturePlotWidget, self).resizeEvent(event)

    def update_plot(self):
        temp = self.sensor.read_temp()
        
        if temp is not None:
            self.temps.append(temp)
            if len(self.temps) > self.max_len:
                self.temps.pop(0)

            self.ax.clear()
            scatter = self.ax.scatter(range(len(self.temps)), self.temps, c=self.temps, cmap=self.cmap, norm=self.norm)
            
            if len(self.temps) > 1:
                self.ax.set_xlim(max(0, len(self.temps) - self.max_len), len(self.temps) - 1)
            else:
                self.ax.set_xlim(-1, 1)  

            self.ax.set_ylim(self.min_temp - 5, self.max_temp + 5)
#             self.ax.set_title(f'Temperature ({int(temp)}°C)', fontsize=7)
            
            self.fig.tight_layout()  # Automatically adjust layout

            self.draw()
        
        QtCore.QTimer.singleShot(500, self.update_plot)


