import subprocess
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

while True:
        input_state = GPIO.input(23)
        if input_state == False:
                print('Downloading XKCD Now')
                subprocess.call("./run.sh", shell=True)
                print('Download XKCD Comic')
                time.sleep(5)
