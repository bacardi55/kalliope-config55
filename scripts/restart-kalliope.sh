#!/bin/sh

kalliope_pid=`ps faux | grep kalliope | grep -v grep | grep -v tee | awk '{print $2}'`
kill "$kalliope_pid"
tmux kill-session -t "kalliope"

tmux new-session -d -s "kalliope" 'cd /home/pi/kalliope_config/ && /usr/bin/python -u /home/pi/kalliope/kalliope.py start | tee kalliope.log'
