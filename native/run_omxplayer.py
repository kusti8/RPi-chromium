#!/usr/bin/env python
import struct
import sys
import json
import subprocess
import urllib2
import os

VERSION=0.4

def check_update():
    new_py = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/RPi-chromium/master/native/run_omxplayer.py").read()
    old_py = open("/usr/bin/run_omxplayer.py").read()
    if new_py is not old_py:
        open("/usr/bin/run_omxplayer.py", 'w').write(new_py)
    subprocess.call("update-youtube.sh", shell=True)

def read_thread_func():
  message_number = 0
  # Read the message length (first 4 bytes).
  text_length_bytes = sys.stdin.read(4)
  # Unpack message length as 4 byte integer.
  text_length = struct.unpack('i', text_length_bytes)[0]
  # Read the text (JSON object) of the message.
  text = sys.stdin.read(text_length).decode('utf-8')
  return text


url = json.loads(read_thread_func())['text']
print 'OK'
subprocess.call("omxplayergui.py ytdl " + url, shell=True)
check_update()
