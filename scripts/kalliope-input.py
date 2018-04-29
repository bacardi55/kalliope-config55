#!/usr/bin/python

import RPi.GPIO as GPIO
import requests
import commands
import time

kalliope_api = {
    'host': 'http://127.0.0.1:5555',
    'credentials': ('bacardi55', 'K@ll1op3'),
    'no_voice': True
}

config = {
    # Mute Kalliope.
    'mute': 17,
    # Unmute Kalliope..
    'unmute': 22,
    # Restart Kalliope.
    'restart': 23,
    # Reboot rpi.
    'reboot': 27
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(config['mute'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(config['unmute'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(config['restart'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(config['reboot'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mute_kalliope(api, mute='True'):
    try:
        resp = requests.post(api['host'] + '/mute',
                             auth = api['credentials'],
                             data = '{"mute": "' + mute + '"}',
                             headers = {'Content-Type': 'application/json'})
        response = resp.json()
        
    except requests.exceptions.RequestException as e:
        pass

def main():
    while True:
        
        if GPIO.input(config['mute']) == False:
            mute_kalliope(kalliope_api, 'True')
            time.sleep(2)

        if GPIO.input(config['unmute']) == False:
            status, output = commands.getstatusoutput("sh /home/pi/kalliope_config/scripts/unmute-kalliope.sh")
            mute_kalliope(kalliope_api, 'False')
            time.sleep(2)

        if GPIO.input(config['restart']) == False:
            status, output = commands.getstatusoutput("sh /home/pi/kalliope_config/scripts/restart-kalliope.sh")
            time.sleep(2)

        if GPIO.input(config['reboot']) == False:
            import os
            status, output = commands.getstatusoutput("sudo reboot")

        time.sleep(0.01)


if __name__ == '__main__':
    main()
