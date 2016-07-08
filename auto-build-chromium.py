from bs4 import BeautifulSoup
import urllib2
from subprocess import call
import os

package_name = ""
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def before():
    global package_name

    page = urllib2.urlopen("http://ports.ubuntu.com/pool/universe/c/chromium-browser/").read()

    soup = BeautifulSoup(page, 'html.parser')
    call("cd ~/chromium-build && git pull", shell=True)
    latest = open("~/chromium-build/url.txt").readline()

    packages = []

    for link in soup.find_all('a'):
        package = link.get('href'))
        if "chromium-browser_" in package:
            packages.append(package)

    for package in packages:
        version = find_between(package, "chromium-browser_", ".")
        if int(version) > int(latest):
            print "FOUND NEW VERSION"
            package_name = package

    call("~/RPi-chromium/copy-package --from=~canonical-chromium-builds/ubuntu/stage --from-suite=trusty --to=~kusti8/ubuntu/chromium-rpi --to-suite=vivid -y chromium-browser", shell=True)

    call('curl -X POST http://textbelt.com/text -d number=**NUMBER** -d "message=Chromium building"', shell=True)

def after():
    global package_name
    call("cd ~/chromium-packages && wget https://launchpad.net/~kusti8/+archive/ubuntu/chromium-rp/+files/"+package_name, shell=True)
    call("cd ~/chromium-packages && wget https://launchpad.net/~kusti8/+archive/ubuntu/chromium-rp/+files/"+"chromium-codecs-ffmpeg-extra_"+find_between(package_name, "chromium-browser_", "deb")+"deb", shell=True)
    call("cd ~/chromium-packages && wget https://launchpad.net/~kusti8/+archive/ubuntu/chromium-rp/+files/"+"chromium-browser-l10n_"+find_between(package_name, "chromium-browser_", ".")+find_between(package_name, "chromium-browser_", "armhf")+"all.deb", shell=True)
    for i in os.listdir(os.getcwd()):
        if i.endswith(".deb"):
            call("curl -T " + i + "-ukusti8:<API_KEY> https://api.bintray.com/content/kusti8/chromium-rpi/chromium-browser/"+<find_between(package_name, "chromium-browser_", ".")+"/"+i+";deb_distribution=jessie;deb_component=test;deb_architecture=armhf", shell=True)
            continue
        else:
            continue
    call("curl -X POST https://maker.ifttt.com...", shell=True)
