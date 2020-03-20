#Simple Radio Server
#A simple radio scheduler that uses external tools (curl, lame) to schedule radio slots by hour...
# =( Coronavirus
import os
import threading
import time
import requests #Maybe i wont use this
import config
import logging
import random

class radio_scheduler(threading.Thread):
    def run(self):
        endpoint = "http://localhost:8000/wnyc"
        print("Started recording at: " + endpoint)
        print(threading.currentThread().getName())
        print(random.randint(0,10) + random.randint(0,10))
        time.sleep(10)


def main():
    for x in range(15):                                   
        #mythread = radio_scheduler(name = "Thread-{}".format(x))
        mythread = radio_scheduler(target="run",args=(1,"http://localhost:8000/wnyc"))
        mythread.start()
        #mythread.run("http://localhost:8000/wnyc")                                   
        #time.sleep(.1)                                   

if __name__ == '__main__':
    main()

    
