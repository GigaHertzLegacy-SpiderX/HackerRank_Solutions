#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    x=[]
    p={')':'(','}':'{',']':'['}
    for a in s:
        if a in p.values():
            x.append(a)
        else:
            if len(x)!=0:
                if p[a]==x[-1]:
                    _=x.pop()
                else:
                    return 'NO'
            else:
                return "NO"    
    else:
        if len(x)==0:
            return "YES"
        return "NO"
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
