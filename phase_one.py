# Phase 1: 
# Create a class that would represent pc parts. It should contain basic methods to retreive items name, price, colour (if applicable).
# PC part list can be found here: https://pcpartpicker.com/list/
# The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
# At this stage, dictionary data structures can work as Database. OOP abstraction, inheritance and encapsulation must be presented in a code base. 
# Unit tests must be written for the methods.


"""PC PART PICKER """
from  parts_database import parts_database
from typing import Dict
from abc import ABC, abstractmethod

class PCPARTS(ABC):
    def __init__(self, name:str, price: float):
        self.name = name
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    
    def  get_price(self) -> float:
        return self.price
    
    @abstractmethod
    def print_smth(self):
        pass
    

class CPU(PCPARTS):
    def __init__(self, name: str, price:float, brand:str, speed:float, power_usage:int):
        super().__init__(name, price)
        self.brand = brand
        self.speed = speed
        self.power_usage = power_usage
        
    @staticmethod
    def get_all_cpus():
        cpu_items = parts_database.get("cpu", {})
        cpu_objects = []
        for item_key, item_data in cpu_items.items():
            cpu = CPU(item_data["name"], item_data["price"], item_data["brand"], item_data["speed"], item_data["power_usage"])
            cpu_objects.append(cpu)
        return cpu_objects       
 
    def get_brand(self):
        return self.brand
    
    def get_speed(self):
        return self.speed
    
    def get_power_usage(self):
        return self.power_usage
    
    
    def print_smth(self):
        return f"CPU Information"
    
    
cpus = CPU.get_all_cpus()


for cpu in cpus:
    print("Name:", cpu.get_name())
    print("Price:", cpu.get_price())
    print("Brand:", cpu.get_brand())
    print("Speed:", cpu.get_speed())
    print("Power Usage:", cpu.get_power_usage())
    print("\n----CPU info-----")