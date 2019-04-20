import unittest
from custom_functions import temperature_methods

class TestCollectionMethods(unittest.TestCase):
    def test_calculate_final_temperature(self):
        list_temperatures = [38, 5, 18, 24, 32]
        temperature = temperature_methods.calculate_final_temperature(list_temperatures)

        self.assertEqual(temperature,23.4)

    def test_calculate_best_temperature(self):
        list_temperature_2=[39,23,56,34,23,24,52,7,]
        temperature_best=temperature_methods.calculate_best_temperature(list_temperature_2)

        self.assertEqual(temperature_best,56)