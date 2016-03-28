#!/usr/bin/env python
import struct
import sys
import json
import subprocess
import urllib2
import os

VERSION="0.5.0"
BRANCH = 'travis'

def check_update():
    #GET PATHS
    pypath = os.getenv('PYPATH', '/usr/bin/run_omxplayer.py')
    manpath = os.getenv('MANPATH', '/etc/chromium-browser/native-messaging-hosts/run_omx.json')
    chromepath = os.getenv('CHROMEPATH', '/usr/bin/install-chromium.sh')
    testing = os.getenv('TESTING', False)

    new_py = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/RPi-chromium/%s/native/run_omxplayer.py" % BRANCH).read()
    old_py = open(pypath).read()
    if new_py != old_py:
        open("run_omxplayer.py", 'w').write(new_py)
        subprocess.call("sudo mv run_omxplayer.py " + pypath + " && sudo chmod +x " + pypath, shell=True)
    new_man = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/RPi-chromium/%s/native/run_omx.json" % BRANCH).read()
    old_man = open(manpath)
    if new_man != old_man:
        open("run_omx.json", "w").write(new_man)
        subprocess.call("sudo mv run_omx.json " + manpath, shell=True)
    subprocess.call("update-ytdl", shell=True)
    old_chrome = open(chromepath).read()
    new_chrome = urllib2.urlopen("https://raw.githubusercontent.com/kusti8/RPi-chromium/%s/install-chromium.sh" % BRANCH).read()
    if new_chrome != old_chrome:
        open("install-chromium.sh", 'w').write(new_chrome)
        subprocess.call("sudo mv install-chromium.sh " + chromepath, shell=True)
        if testing == False:
            subprocess.call("install-chromium.sh", shell=True)

def check_arguments():
#open('/home/pi/test', 'w').write(''.join(sys.argv))
    if len(sys.argv) > 1:
        if sys.argv[1] == '-U':
            check_update()
            sys.exit(0)
    else:
        print "Invalid command line option!\nTo update: run_omxplayer.py -U"
        sys.exit(-1)
    return True

def read_thread_func():
  message_number = 0
  # Read the message length (first 4 bytes).
  text_length_bytes = sys.stdin.read(4)
  # Unpack message length as 4 byte integer.
  text_length = struct.unpack('i', text_length_bytes)[0]
  # Read the text (JSON object) of the message.
  text = sys.stdin.read(text_length).decode('utf-8')
  return text

def run_main():
    url = json.loads(read_thread_func())['text']
    print 'OK'
    subprocess.call("omxplayergui ytdl " + url, shell=True)

if __name__ == "__main__":
    check_arguments()
    run_main()
