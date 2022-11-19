import subprocess

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import time
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

from threading import Thread
from kivy.clock import Clock


# cpu_command = "top -b -n 1 | awk '{print $9}'| tail -n+8 | awk '{s+=$1} END {print s}'"    # <-- not sure why not work
# cpu_command = "bash exec.sh"      # <-- refreshing does not work because variables in script do not change
cpu_command = "head -n1 /proc/stat"     # <-- not finished because this command needs sudo on android...
cpu_usage = 0

# battery_state = "Charging"
# battery_capacity = "100"

stop_threads = False


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(MDLabel(text='CPU'))
        self.cpuValues = CpuWidget()
        self.add_widget(self.cpuValues)
        # self.add_widget(MDLabel(text='Battery capacity'))
        # self.battery_capacity = BatteryCapacity()
        # self.add_widget(self.battery_capacity)
        # self.add_widget(MDLabel(text='Battery status'))
        # self.battery_state = BatteryState()
        # self.add_widget(self.battery_state)
        # self.OCRButton = Button(text= "OCR Not implemented")
        # self.add_widget(self.OCRButton)
        # self.OCRtext = TextInput(multiline=False)
        # self.add_widget(self.OCRtext)


def get_cpu():
    global core_num, core_dict, stop_threads, cpu_usage

    while True:
        time.sleep(0.3)
        cpu_usage = subprocess.check_output(cpu_command, shell=True)
        if stop_threads:
            print("stop")
            break


# def get_battery():
#     global battery_state, battery_capacity, stop_threads
#
#     while True:
#         time.sleep(0.3)
#         current_status = psutil.sensors_battery()
#         battery_state = "Charging" if current_status.power_plugged else "Discharging"
#         battery_capacity = f"{current_status.percent}"
#         if stop_threads:
#             print("stop")
#             break


class CpuUsageCore(MDLabel):

    def __init__(self, **kwargs):
        super(CpuUsageCore, self).__init__(**kwargs)
        self.text = "Usage = " + str(cpu_usage) + "%"
        Clock.schedule_interval(self.update, 0.5)
        self.halign = 'center'

    def update(self, *args):
        self.text = "Usage = " + str(cpu_usage) + "%"


class CpuWidget(GridLayout):

    def __init__(self, **kwargs):
        super(CpuWidget, self).__init__(**kwargs)
        self.id = 'cpuWidget'
        self.cols = 1
        self.add_widget(CpuUsageCore())

# class BatteryState(MDLabel):
#
#     def __init__(self, **kwargs):
#         super(BatteryState, self).__init__(**kwargs)
#         self.text = battery_state
#         Clock.schedule_interval(self.update, 1)
#         self.halign = 'center'
#
#     def update(self, *args):
#         self.text = battery_state
#
#
# class BatteryCapacity(MDLabel):
#
#     def __init__(self, **kwargs):
#         super(BatteryCapacity, self).__init__(**kwargs)
#         self.text = battery_capacity
#         Clock.schedule_interval(self.update, 1)
#         self.halign = 'center'
#
#     def update(self, *args):
#         self.text = battery_capacity


class MyApp(MDApp):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    get_cpu_thread = Thread(target=get_cpu)
    get_cpu_thread.daemon = True
    get_cpu_thread.start()

    # get_battery_thread = Thread(target=get_battery)
    # get_battery_thread.daemon = True
    # get_battery_thread.start()
    MyApp().run()
