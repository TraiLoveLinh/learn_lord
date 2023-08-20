# Enter your code here. Read input from STDIN. Print output to STDO
import math
import os
import random
import re
import sys

queue = []
n = int(input())
for _ in range(n):
    inp = input().split()
    if len(inp) == 1:
        tp = int(inp[0])
        if tp == 2:
            del queue[0]
        elif tp == 3:
            print(queue[0])
    else:
        tp, x = int(inp[0]), int(inp[1])
        queue.append(x)
