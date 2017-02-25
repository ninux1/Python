#!/usr/bin/env python

# See the map function below.

temp_data = (36.5, 37, 37.5, 39)

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

F = map(fahrenheit, temp_data)
C = map(celsius, F)

print "Fahrenhit = ", F
print "Celsius = ", C
