#!/bin/sh
cd `dirname $0` || exit 1
/usr/bin/python3.6 ./run.py >> xxoovideo.log 2>&1
