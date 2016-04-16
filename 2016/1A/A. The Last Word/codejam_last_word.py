with open("A-large-practice-last-word.in", "r") as f:
    cases = int(f.readline())

    for i in range(cases):
        S = str(f.readline())
        result = ""

        for c in S:
            if result == "":
                result = c
            elif result != "" and result[0] > c:
                result = result + c
            elif result != "" and result[0] <= c:
                result = c + result

        print "Case #%i: " % (i + 1) + result,
