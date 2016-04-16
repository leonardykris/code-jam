# Google Code Jam 2016
# Problem A: Counting Sheep

# Logic:
# 1. Create a dictionary (D) with the number 0-9 as keys with all values initialized to False
# 2. Open file
# 3. Scan for the number of test cases (T) being offered in the first line to get the range
# 4. Scan the next line, record the value (N)
# 5. If N is 0: print INSOMNIA because it won't ever fulfil the requirements
# 6. If N is not 0: for each digits in N, use the current digit as a key to toggle the value in D
# 7. Run a check on D to see whether all keys are toggled to True. If the condition is fulfilled, print N and continue to the next case, repeat step 4-8
# 8. Multiply N by i, repeat step 6-7



# Google Code Jam 2016
# Problem B: Revenge of the Pancakes

# Logic:
# 1. Scan the input, record
# 2. Check per character, if it's -, then continue, if it's + at index i, it means all the minus behind has to be flipped (0 to i-1) to +, then flip all the plus to minus (0 to i)
# 1. Repeat 2 until end of line reached, then do one last flipping to make it all plus
# 1.
# 1.
# 1.
# 1.
# 1.