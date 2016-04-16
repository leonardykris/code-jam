# Imports
import math
# or from math import sqrt
# or from math import *
# check from dir(math)

# All simple calculation modes
def multiply(first_num, second_num):
  return first_num * second_num

def add(first_num, second_num):
  return first_num + second_num

def subtract(first_num, second_num):
  return first_num - second_num

def divide(first_num, second_num):
  return first_num / second_num

def modulo(first_num, second_num):
  return first_num % second_num

# Accept input function
def acceptInput(order):
  try:
    input = int(raw_input("Enter the %s number: " % (order)))
    return input
  except ValueError:
    print "That's not a valid number (0-9), you see. Please try again."
    return acceptInput(order)

def getCalculatorMode():
  try:
    mode = int(raw_input("Please choose calculator mode (1-5): "))
    if not (1 <= mode <= 5):
      raise ValueError()
  except ValueError:
    print "Invalid input, please try again."
    return getCalculatorMode()
  else:
    print "You have chosen mode ", mode

# Calculator function
def calculator():
  print "============================"
  print "This is a calculator program"
  print "============================"
  print "Available modes:"
  print "1. Addition"
  print "2. Subtraction"
  print "3. Multiplication"
  print "4. Division"
  print "5. Modulo"

  mode = getCalculatorMode()

  first = acceptInput("first")
  second = acceptInput("second")

  print "Result: ", multiply(first, second)

# Call calculator function
calculator()