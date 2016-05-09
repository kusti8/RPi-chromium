if grep -q "http://dl.bintray.com/kusti8/chromium-rpi" /etc/apt/sources.list; then
  sudo apt-get update
  sudo apt-get install chromium-browser kweb -y
else
  wget -qO - http://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
  echo "deb http://dl.bintray.com/kusti8/chromium-rpi jessie main" | sudo tee -a /etc/apt/sources.list
  sudo apt-get update
  sudo apt-get install chromium-browser kweb -y
fi  
sudo cp native/run_omxplayer.py /usr/bin/
sudo cp native/start_ytdl_server.sh /usr/bin
sudo mkdir /etc/chromium-browser/native-messaging-hosts
sudo cp native/run_omx.json /etc/chromium-browser/native-messaging-hosts/
chromium-browser chrome://extensions &
sudo leafpad /etc/chromium-browser/native-messaging-hosts/run_omx.json

