#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
if __name__ == '__main__':
    hh = int (input())
    mm = int (input())
    map1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',16:"sixteen",17:'seventeen',18:"eighteen",19:'nineteen',20:'twenty',40:"fourty",50:"fifty"}
    map2={15:'quarter',30:'half',45:'quarter'}
    if(mm==0):
        print("{0} o' clock".format(map1.get(hh)))

    elif ( mm%15==0):
        if(mm<=30):
            print("{0} past {1}".format(map2.get(mm),map1.get(hh)))
        else:
            print("{0} to {1}".format(map2.get(mm),map1.get((hh%12)+1)))
    else:
        if(mm%10==0):
            if(mm<30):
                print("{0} minutes past {1}".format(map1.get(mm),map1.get(hh)))
            else:
                mm=60-mm
                print("{0} minutes to {1}".format(map1.get(mm),map1.get((hh%12)+1)))
        elif(mm>20):
            a =int(mm/10)*10
            b = mm%10
            if(mm<30):
                print("{0} {2} minutes past {1}".format(map1.get(a),map1.get(hh),map1.get(b)))
            else:
                mm=60-mm
                if(mm>20):
                    a =int(mm/10)*10
                    b = mm%10
                    print("{0} {2} minutes to {1}".format(map1.get(a),map1.get((hh%12)+1),map1.get(b)))
                else:
                    print("{0} minutes to {1}".format(map1.get(mm),map1.get((hh%12)+1)))
        else:
            print("{0} minute past {1}".format(map1.get(mm),map1.get(hh)))
    
