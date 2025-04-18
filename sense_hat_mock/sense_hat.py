# Mock implementation of the Raspberry Pi Sense HAT API
import random


class SenseHat:
    def __init__(self):
        self._led_matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

    @property
    def temperature(self):
        return 22.5  # Always return 22.5°C

    @property
    def humidity(self):
        return 45.0  # Always return 45% humidity

    @property
    def pressure(self):
        return 1013.25  # Always return 1013.25 hPa

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def set_pixels(self, pixel_list):
        if len(pixel_list) == 64:
            self._led_matrix = [pixel_list[i * 8 : (i + 1) * 8] for i in range(8)]

    def clear(self):
        self._led_matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

    def show_message(self, message, text_colour=(255, 255, 255), back_colour=(0, 0, 0)):
        print(f"Mock display: {message}")
