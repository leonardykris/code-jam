# Google Code Jam 2016
# Problem A: Counting Sheep
# Author: Leonardy Kristianto (leonardy)

with open("A-large.in", "r") as f:
  cases = int(f.readline())
  print "range:", cases

  for i in range(cases):
    dictionary = {
      '0': False,
      '1': False,
      '2': False,
      '3': False,
      '4': False,
      '5': False,
      '6': False,
      '7': False,
      '8': False,
      '9': False,
    }

    count = 1
    sleep = False
    num = int(f.readline())

    if num == 0:
      print "Case #%i: INSOMNIA" % (i + 1)
    else:
      while sleep == False:
        for digit in str(num * count):
          dictionary[digit] = True

        for key in dictionary:
          if dictionary[key] == False:
            break
        else:
          print "Case #%i: %i" % (i + 1, num * count)
          sleep = True

        count += 1

