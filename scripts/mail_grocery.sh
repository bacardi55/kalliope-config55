#!/bin/bash

set -x

./sendmail.py -s="[kalliope] Liste de courses" -b="`grep +course ~/todo.txt`"
