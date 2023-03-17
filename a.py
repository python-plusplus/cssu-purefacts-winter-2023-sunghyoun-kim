import csv
import math

def maxTime(fs):
    mc = -math.inf
    st = ''
    ed = ''
    m = 0
    with open(fs, newline='') as csvfile:
        creader = csv.reader(csvfile, delimiter=',')
        for row in creader:
            if row[1] != "StartTime":
                a = int(row[1].replace(':', '')) 
                b = int(row[2].replace(':', ''))
                if a > 900 and a < 1700 and b > 900 and b < 1700:
                    mc = max(b - a, mc);
                    st = row[1];
                    ed = row[2];
                    m = (math.floor(b / 100) - math.floor(a / 100) - 1) * 60 + (60 - (a % 100)) + (b % 100) 
        if mc == -math.inf or mc <= 0:
            return None
        else:
            return (st, m)

