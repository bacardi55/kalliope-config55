#!/usr/bin/python
# coding: utf-8

import subprocess
import sys

alarm_clock_path = "/home/pi/kalliope_config/scripts/wakeup.sh"

def main():

    # print 'Args:', str(sys.argv)

    args = sys.argv[1].split()
    # print args
    # print(args[2])

    # Command to be run after the needed time
    # Update your API info for this command to work.
    bashCommand = "at -M -f " + alarm_clock_path + " #REMINDER_TIME# "
    # bashCommand = """at -M #REMINDER_TIME# << EOF
    # curl -i --user "admin":"secret" -H "Content-Type: application/json" -X POST -d '{"order":"api-repeat-cmd #MESSAGE#"}' http://localhost:5000/synapses/start/order
    # EOF"""

    # Query pattern:
    # à {{heures}}:{{minutes}}

    # Mispelling on purpose to force right pronounciation and avoid charset issue
    message = "Monsieur, vous mavez demander de vous réveiller à "
    end_message = ""

    # If the reminder is at a specific time
    # TODO
    reminder_time = args[0]
    # print(reminder_time)

    # for "o'clock" hours, need to add 00 minute for the at command to work
    if len(reminder_time) <= 3:
        reminder_time += "00"

    # Mispelling on purpose to force right pronounciation and avoid charset issue
    end_message = "Reveil programmer a " + reminder_time

    bashCommand = bashCommand.replace("#REMINDER_TIME#", reminder_time)
    # print(bashCommand)

    p = subprocess.Popen(bashCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # for Kalliopé to read:
    print end_message


if __name__ == "__main__":
    main()

