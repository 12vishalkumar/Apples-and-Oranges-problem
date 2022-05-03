import math
import os
import random
import re
import sys
# Complete the 'countApplesAndOranges' function below.
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    Apple = []
    Orange = []
    Ac = Oc = 0
    for i in apples:
        Apple.append(a+i)
    for j in oranges:
        Orange.append(b+j)
    for i in Apple:
        if(i>=s and i<=t):
            Ac += 1
    print(Ac)
    for i in Orange:
        if(i>=s and i<=t):
            Oc += 1
    print(Oc)
    return 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
