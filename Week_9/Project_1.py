import random
import tkinter as tk
from tkinter import messagebox
employees = ["Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
             "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo",
             "Abraham Jones", "Nicole Anide", "Kosi Korso", "Adele Martins",
             "Emmanuel Ojo", "Ajayi Fatima"]

tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]


class Employee():

    def __init__(self, name):
        self.name = name

    def check_employee(self):
        if self.name in employees:
            emp.take_attendance()
            emp.assign_task()
        else:
            emp.refuse_access()
    def take_attendance(self):
        print(f"Welcome {self.name}, you have been marked present")

    def assign_task(self):
        random_number = random.randint(0,4)
        print(f"Your task for today Mr/Mrs {self.name} will be {tasks[random_number]}")

    def refuse_access(self):
        print(f"{self.name}, You are not an employee at this establishment, please exit the premises, thank you.")


emp = Employee(input("Enter the name on your Employee ID: "))
emp.check_employee()

