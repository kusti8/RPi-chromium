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
    new_man = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/RPi-chromium/master/native/run_omx.json").read()
    old_man = open("/etc/chromium-browser/native-messaging-hosts/run_omx.json")
    if new_man is not old_man:
        open("/etc/chromium-browser/native-messaging-hosts/run_omx.json", "w").write(new_man)
    subprocess.call("update-ytdl", shell=True)



if sys.argv[1] == "-U":
    check_update()
    print "Done with the update! If any error, remember to use sudo run_omxplayer.py!!!"
    sys.exit(0)
elif len(sys.argv) == 1:
    pass
else:
    print "Invalid command line option!\nTo update: run_omxplayer.py -U"
    
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
