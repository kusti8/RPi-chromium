Y_LOC = $HOME
sudo -s <<EOF
apt-get install omxplayer -y
CURRENT=$(pwd)
HOME = $Y_LOC
wget **URL**
tar -xzf **FILE**
cd **FOLDER**
./installomxplayergui
ginstall-ytdl
ln -s "$CURRENT/native/run_omxplayer.py" /usr/bin/run_omxplayer.py
mkdir /etc/chromium-browser/native-messaging-hosts
cp "$CURRENT/native/run_omx.json" /etc/chromium-browser/native-messaging-hosts/run_omx.json
echo "Done! Now install the RPi-youtube extension."
EOF
