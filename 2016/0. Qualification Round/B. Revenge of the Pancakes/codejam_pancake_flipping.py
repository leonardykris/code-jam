# Google Code Jam 2016
# Problem B: Revenge of the Pancakes
# Author: Leonardy Kristianto (leonardy)

def flip(stack, start, end):
  for index, side in enumerate(stack[start:end]):
    if side == "+":
      stack[index] = "-"
    elif side == "-":
      stack[index] = "+"
  return "".join(stack)

def getChangePoint(stack):
  for index, side in enumerate(stack):
    if index <= len(stack) - 2:
      if stack[index] == "-" and stack[index + 1] == "+":
        return index
      elif stack[index] == "+" and stack[index + 1] == "-":
        return index
  else:
    return -1

with open("B-large.in", "r") as f:
  cases = int(f.readline())

  for i in range(cases):
    count = 0
    allHappy = False
    stack = str(f.readline()) # this is the initial stack

    while allHappy == False:
      changePoint = getChangePoint(stack)

      if changePoint != -1:
        stack = flip(list(stack), 0, changePoint + 1) # on - then +
        count += 1
      elif changePoint == -1 and stack[0] == "-": # all -
        stack = flip(list(stack), 0, len(stack))
        count += 1
        allHappy = True
      elif changePoint == -1 and stack[0] == "+": # all already +
        allHappy = True

    print "Case #%i: %i" % (i + 1, count)

