# Google Code Jam 2016
# Problem C: Coin Jam
# Author: Leonardy Kristianto (leonardy)

import random


def checkPrime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= num:
        if num % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def getDivisor(num):
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= num:
        # print i, num
        if num % i == 0:
            return i

        i += w
        w = 6 - w


def makeRandomBinary(digits):
    pattern = "".join(str(random.randint(0, 1)) for x in range(digits - 2))
    return "1" + pattern + "1"

with open("coinjam.in", "r") as f:
    cases = int(f.readline())

    for i in range(cases):
        N, J = str(f.readline()).split()
        # example dataset: N = 6, J = 3
        validSerial = 0
        collection = []

        print "Case #%i:" % (i + 1)

        while validSerial != int(J):
            serial = makeRandomBinary(int(N))
            divisors = []

            for j in range(2, 11):
                sum = 0
                for index, c in enumerate(str(serial)):
                    if int(c) == 1:
                        value = j ** (int(N) - (index + 1))
                        sum += value
                # print "[", sum, "]", "Prime:", checkPrime(sum)
                if checkPrime(sum) is True:
                    break
                else:
                    divisors.append(str(getDivisor(sum)))
                    # print getDivisor(sum),
            else:
                if serial in collection:
                    # print "Serial already exists"
                    pass
                else:
                    collection.append(serial)
                    # put a check here whether serial has existed in collection
                    validSerial += 1
                    print serial, ' '.join(divisors)
                    # print collection
