# Mock implementation of the Raspberry Pi Sense HAT API
import random


class SenseHat:
    def __init__(self):
        self._led_matrix = [[(0, 0, 0) for _ in range(8)] for _ in range(8)]

    @property
    def temperature(self):
        return random.uniform(15.0, 30.0)

    @property
    def humidity(self):
        return random.uniform(30.0, 70.0)

    @property
    def pressure(self):
        return random.uniform(980.0, 1050.0)

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
        print(f"Mock show_message: {message}")


# ...add more mock methods as needed for your use case...
