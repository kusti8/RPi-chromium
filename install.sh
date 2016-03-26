sudo -s <<EOF
apt-get install omxplayer -y
EOF
wget http://steinerdatenbank.de/software/kweb-1.7.0.tar.gz
tar -xzf kweb-1.7.0.tar.gz
cd kweb-1.7.0
yes | ./debinstall
sudo -s <<EOF
cd ..
cd ..
cp native/run_omxplayer.py /usr/bin/run_omxplayer.py
mkdir /etc/chromium-browser/native-messaging-hosts
cp native/run_omx.json /etc/chromium-browser/native-messaging-hosts/run_omx.json
echo "Done! Now install the RPi-youtube extension."
EOF
