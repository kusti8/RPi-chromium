sudo apt-get install git omxplayer -y
git clone git://github.com/rg3/youtube-dl
cd /usr/bin
sudo ln -s /home/pi/RPi-chromium/youtube-dl/youtube_dl/__main__.py youtube-dl
cat > update-youtube.sh << EOF

sudo ln -s /home/pi/RPi-chromium/native/run_omxplayer.py /usr/bin/run_omxplayer.py
sudo mkdir /etc/chromium-browser/native-messaging-hosts
sudo cp /home/pi/RPi-chromium/native/run_omx.json /etc/chromium-browser/native-messaging-hosts/run_omx.json
echo "Done! Now install the RPi-youtube extension."
