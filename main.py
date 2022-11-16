from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import time
import psutil
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

from threading import Thread
from kivy.clock import Clock
from sympy import true


core_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
core_num = 8
battery_state = "Charging"
battery_capacity = "100"

stop_threads = False


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(MDLabel(text='CPU'))
        self.cpuValues = CpuWidget()
        self.add_widget(self.cpuValues)
        self.add_widget(MDLabel(text='Battery'))
        self.password = BatteryCapacity()
        self.add_widget(self.password)
        self.OCRButton = Button(text= "OCR Not implemented")
        self.add_widget(self.OCRButton)
        self.OCRtext = TextInput(multiline=False)
        self.add_widget(self.OCRtext)

def get_cpu():
    global core_num, core_dict, stop_threads

    while True:
        time.sleep(0.3)
        cpu_use = psutil.cpu_percent(2, True)
        core_num = len(cpu_use)
        for i in range(core_num):
            core_dict.update({i + 1: cpu_use[i]})
        if stop_threads:
            print("stop")
            break


def get_battery():
    global battery_state, battery_capacity, stop_threads

    while True:
        time.sleep(0.3)
        battery_state = open("/sys/class/power_supply/BAT0/status", "r").readline().strip()
        battery_capacity = open("/sys/class/power_supply/BAT0/capacity", "r").readline().strip()
        if stop_threads:
            print("stop")
            break

class CpuUsageCore(MDLabel):

    def __init__(self, core, **kwargs):
        super(CpuUsageCore, self).__init__(**kwargs)
        self.core = core
        self.text = "CPU " + str(self.core) + "    " + str(core_dict[self.core]) + "%"
        Clock.schedule_interval(self.update, 0.5)
        self.halign = 'center'

    def update(self, *args):
        self.text = "CPU " + str(self.core) + "    " + str(core_dict[self.core]) + "%"


class CpuWidget(GridLayout):

    def __init__(self, **kwargs):
        super(CpuWidget, self).__init__(**kwargs)
        self.id = 'cpuWidget'
        self.cols = 1
        for i in range(core_num):
            self.add_widget(CpuUsageCore(i + 1))

class BatteryState(MDLabel):

    def __init__(self, **kwargs):
        super(BatteryState, self).__init__(**kwargs)
        self.text = battery_state
        Clock.schedule_interval(self.update, 1)
        self.halign = 'center'

    def update(self, *args):
        self.text = battery_state


class BatteryCapacity(MDLabel):

    def __init__(self, **kwargs):
        super(BatteryCapacity, self).__init__(**kwargs)
        self.text = battery_capacity
        Clock.schedule_interval(self.update, 1)
        self.halign = 'center'

    def update(self, *args):
        self.text = battery_capacity


class MyApp(MDApp):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    get_cpu_thread = Thread(target=get_cpu)
    get_cpu_thread.daemon = True
    get_cpu_thread.start()

    get_battery_thread = Thread(target=get_battery)
    get_battery_thread.daemon = True
    get_battery_thread.start()
    MyApp().run()