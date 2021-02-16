import math
import os
import random
import re
import sys

def counting_valleys(steps, path):
    stack = []
    valleys = 0
    for i in path:
        if not stack:
            stack.append(i)
        elif stack[-1] == 'U' and i == 'U':
            stack.append(i)
        elif stack[-1] == 'D' and i == 'D':
            stack.append(i)
        elif stack[-1] == 'U' and i == 'D':
            stack.pop()
        else:
            stack.pop()
            if not stack:
                valleys += 1
    
    return valleys


if __name__ == "__main__":
    steps = 8
    path = "UDDDUDUU"

    print(counting_valleys(steps, path))