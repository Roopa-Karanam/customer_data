# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:38:22 2022

@author: karan
"""

name=input("Hello there\n please enter your name: ")
age=int(input("Enter your age: "))
location=input("Enter your location: ")
department=input("Enter your department: ")

customer_data={
    "Name":name,
    "Age":age,
    "Location":location,
    "Department":department
    
    }

print("Here is your data: ", customer_data)