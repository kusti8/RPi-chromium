#!/usr/bin/env python
import struct
import sys
import json
import subprocess
import urllib2

VERSION=0.1

open('/home/pi/test', 'w').write('hi')

def check_update():
    new_py = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/Rpi-youtube/master/native/run_omxplayer.py").read()
    old_py = open("/usr/local/bin/run_omxplayer.py").read()
    if new_py is not old_py:
        open("/usr/local/bin/run_omxplayer.py", 'w').write(new_py)

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
process = subprocess.Popen(['youtube-dl', '-g', url], stdout=subprocess.PIPE)
video_url,err = process.communicate()
subprocess.call(['omxplayer', video_url])
check_update()
