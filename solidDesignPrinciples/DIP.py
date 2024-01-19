
# DIP-> The Dependency Inversion Principle consists of two key guidelines:
#1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
#2. Abstractions should not depend on details. Details should depend on abstractions.

# Violation of DIP

class LightBulb:
    def turn_on(self):
        # specific implementation to turn on the light bulb
        pass

class Switch:
    def operate(self, bulb):
        bulb.turn_on()

# Adhering to DIP

from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        # specific implementation to turn on the light bulb
        pass

class Switch:
    def operate(self, device):
        device.turn_on()
