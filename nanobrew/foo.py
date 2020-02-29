import time
import threading

def read_temperatures():
    while True:
        print("Hoi")
        time.sleep(1)

def read_sensors():
    thread = threading.Thread(target = read_temperatures)
    thread.start()