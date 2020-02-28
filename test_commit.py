#! /usr/bin/python3

import time

def next_num():
    try:
        f = open("/myfile", "r")
        n = int(f.readline())
        f.close()
    except Exception as e:
        n = 0
    print(n)
    n = n+1
    f = open("/myfile", 'w')
    f.seek(0)
    f.write(str(n))
    f.close()
    f = open("myfile", 'w')
    f.seek(0)
    f.write(str(n))
    f.close()

if __name__ == '__main__':
    while True:
        next_num()
        time.sleep(5)
    
