# Phase 1: 
# Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).
# PC part list can be found here: https://pcpartpicker.com/list/
# The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
# At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base. 
# Unit tests must be written for the methods.


"""PC PART PICKER """
from parts_database import parts_database
from typing import Dict
from abc import ABC, abstractmethod

class PCPARTS(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price
    
    @abstractmethod
    def print_additional_info(self):
        pass
    

class CPU(PCPARTS):
    def __init__(self, name: str, price: float, brand: str, speed: float, power_usage: int):
        super().__init__(name, price)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage
        
    @staticmethod
    def get_all_cpus():
        cpu_items = parts_database.get("cpu", {})
        cpu_objects = []
        for item_key, item_data in cpu_items.items():
            cpu = CPU(
                item_data["name"], item_data["price"], item_data["brand"],
                item_data["speed"], item_data["power_usage"]
            )
            cpu_objects.append(cpu)
        return cpu_objects
    
    def get_brand(self) -> str:
        return self.brand
    
    def get_speed(self) -> float:
        return self.speed
    
    def get_power_usage(self) -> int:
        return self.power_usage
    
    def print_additional_info(self):
        return f"CPU Information"
    

class CPUCooler(PCPARTS):
    def __init__(self, name: str, price: float, cooler_type: str, noise_level: float):
        super().__init__(name, price)
        self.cooler_type = cooler_type
        self.noise_level = noise_level
        
    @staticmethod
    def get_all_cpu_coolers():
        cpu_cooler_items = parts_database.get("cpu_cooler", {})
        cpu_cooler_objects = []
        for item_key, item_data in cpu_cooler_items.items():
            cpu_cooler = CPUCooler(
                item_data["name"], item_data["price"], item_data["cooler_type"],
                item_data["noise_level"]
            )
            cpu_cooler_objects.append(cpu_cooler)
        return cpu_cooler_objects

    def print_additional_info(self):
        return f"CPUCooler Information"


cpus = CPU.get_all_cpus()
print(cpus)

for cpu in cpus:
    print("\n----CPU info-----\n")
    print("Name:", cpu.get_name())
    print("Price:", cpu.get_price())
    print("Brand:", cpu.get_brand())
    print("Speed:", cpu.get_speed())
    print("Power Usage:", cpu.get_power_usage())


cpu_coolers = CPUCooler.get_all_cpu_coolers()
print(cpu_coolers)

for cpu_cooler in cpu_coolers:
    print("\n----CPU Cooler info-----\n")
    print("Name:", cpu_cooler.get_name())
    print("Price:", cpu_cooler.get_price())
    print("Cooler Type:", cpu_cooler.cooler_type)
    print("Noise Level:", cpu_cooler.noise_level)