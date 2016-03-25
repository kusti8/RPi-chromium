Y_LOC = $HOME
sudo -s <<EOF
apt-get install omxplayer -y
CURRENT=$(pwd)
HOME = $Y_LOC
wget http://steinerdatenbank.de/software/kweb-1.6.9.tar.gz
tar -xzf kweb-1.6.9.tar.gz
cd kweb-1.6.9
./debinstall
ginstall-ytdl
wget http://steinerdatenbank.de/software/omxplayergui-1.7-beta-5.tar.gz
tar -xzf omxplayergui-1.7-beta-5.tar.gz
cd omxplayergui-1.7-beta-5
sudo ./install
cp "$CURRENT/native/run_omxplayer.py" /usr/bin/run_omxplayer.py
mkdir /etc/chromium-browser/native-messaging-hosts
cp "$CURRENT/native/run_omx.json" /etc/chromium-browser/native-messaging-hosts/run_omx.json
echo "Done! Now install the RPi-youtube extension."
EOF
