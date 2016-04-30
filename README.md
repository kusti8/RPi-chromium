# RPi-chromium 
Chromium tools for the Raspberry Pi. This includes RPi-youtube which uses omxplayerGUI to play youtube videos at the click of a button. More info can be found in the slowly growing Wiki.

## Feature requests? Open an issue!

## Install
First clone this: `git clone https://github.com/kusti8/RPi-chromium`
Then, change into it: `cd RPi-chromium`
You must have Chromium installed: https://www.raspberrypi.org/forums/viewtopic.php?t=121195
To install the local youtube extension, run this:
`./install.sh`
The installer will install youtube-dl and the native script. **You must install the chrome extension!** https://chrome.google.com/webstore/detail/rpi-youtube/laacchpjldmpbhkcjfmfcjijaekhhlgn

## What is this?
This is currently a git for various Chromium additions to make it run smoother on the raspberry pi, starting with the youtube local extension. It is currently in beta, but getting more stable.

## Limitations
Right now, it's bare minimum. Some omxplayer options cannot be changed through the script, but through omxplayerGUI options, which are a little less intuitive. 


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/kusti8/rpi-chromium/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

