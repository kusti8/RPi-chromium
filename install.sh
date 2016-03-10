sudo apt-get install git omxplayer -y
git clone git://github.com/rg3/youtube-dl
git clone git://github.com/kusti8/Rpi-youtube
cd /usr/bin
sudo ln -s ~/youtube-dl/youtube_dl/__main__.py youtube-dl
sudo ln -s ~/youtube-omxplayer/native/run_omxplayer.py /usr/local/bin/run_omxplayer.py
sudo cp native/run_omx.json /etc/chromium/native-messaging-hosts/run_omx.json
echo "Done! Now install the RPi-youtube extension."
