#Simple Radio Server
#A simple radio scheduler that uses external tools (curl, lame) to schedule radio slots by hour...
# =( Coronavirus
import os
import threading
import time
import datetime
import requests #Maybe i wont use this
import config
import logging
import random

class radio_scheduler(threading.Thread):
    def run(self):
        #endpoint = "http://localhost:8000/wnyc"
        print("Started recording at: " + endpoint)
        print(threading.currentThread().getName())
        print(random.randint(0,10) + random.randint(0,10))
        time.sleep(10)

    def recording_thread(self):
        start_time = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        kill_time = time.time #next hour
        proc = subprocess.Popen("curl http://localhost:8000/wnyc > " )
        while (time.time <= kill_time) {
            #do_nothing
        }
        proc.kill()






def main():
    endpoint = "http://localhost:8000/wnyc"

if __name__ == '__main__':
    main()

    
