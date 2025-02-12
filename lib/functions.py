#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")
    return(greet_programmer)
 

def greet(name):
    print(f"Hello, {name}!")
    return(greet)
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return(greet_with_default)



def add(num1, num2):
    print(num1 + num2)
    return(45 + 55)


def halve(number):
    return(number / 2)
