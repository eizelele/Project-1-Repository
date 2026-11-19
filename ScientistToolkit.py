
from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod

    def get_reading(self):

        pass

class TempSensor(Sensor):

    def get_reading (self):

        print("[Temperature Sensor] Reading: 24.5°C")

class PHSensor(Sensor):
    def get_reading(self):
        print("[pH Sensor] Reading: 7.2 pH (Neutral)")




print("--- Lab Inventory System ---")
sensor1 = TempSensor()
sensor2 = PHSensor()
sensor2.get_reading()
sensor1.get_reading()

