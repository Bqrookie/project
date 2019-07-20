# encoding: utf-8
import requests
import time

for i in range(1111):
    time.sleep(1)
    print("\r Loading... ".format(i)+str(i), end="")