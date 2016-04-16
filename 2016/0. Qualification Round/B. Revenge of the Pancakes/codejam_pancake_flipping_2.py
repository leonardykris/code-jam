# Google Code Jam 2016
# Problem B: Revenge of the Pancakes
# Author: Leonardy Kristianto (leonardy)

with open("pancakes.in", "r") as f:
  cases = int(f.readline())
  # print "range:", cases

  for i in range(cases):
    count = 0
    allHappy = False
    stack = str(f.readline()) # this is the initial stack

    for index, side in enumerate(stack):
      if stack[index] == "-" and stack[index + 1] == "+":
        if index != 1 # means there are other elements behind
          for
          stack[index] = "+" # flip
      elif stack[index] == "+" and stack[index + 1] == "-":
        stack[index] = "-" # flip