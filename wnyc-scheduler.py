#ICECast streamer
# v1.0 -- just get it working for now
# =( Coronavirus
import os
import sys
import datetime
import time
import subprocess
import requests
import threading

class capture_worker:
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def capture(self):
        start_time = datetime.datetime.now()
        #kill_time = start_time.replace(minute=0,second=0,microsecond=0)
        #kill_time = kill_time + datetime.timedelta(hours=1)
        doc = requests.get('./pub' + 'http://10.0.0.44:8000/wnyc', stream=True)
        with open(('wnyc-' + start_time.strftime("%y%m%d-%H%M%S") + '.mp3'),'wb') as f:
            for chunk in doc.iter_content(chunk_size=1024*36):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    if (self._running == False): doc.close()
        doc.close()
        self.running= False



def main():
    while (True):
        start_time = datetime.datetime.now()
        kill_time = start_time.replace(minute=0,second=0,microsecond=0)
        kill_time = kill_time + datetime.timedelta(hours=1)
        worker = capture_worker()
        thread = threading.Thread(target = worker.capture)
        thread.start()
        while (datetime.datetime.now() <= kill_time):
            time.sleep(1)
    
        worker.terminate()
        #thread.join() #Do i really need this? just start another thread right?

if __name__ == '__main__':
    main()

    
