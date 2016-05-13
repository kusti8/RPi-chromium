FROM armhf/debian:jessie

RUN apt-get update
RUN echo "deb-src http://ports.ubuntu.com/ trusty multiverse universe main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get build-dep chromium-browser
RUN apt-get install nano wget devscripts debhelper build-essential git exfat-fuse exfat-utils python-virtualenv python
RUN cd
RUN mkdir -p tmp/buildbot
RUN virtualenv --no-site-packages sandbox
RUN source sandbox/bin/activate
RUN easy_install sqlalchemy==0.7.10
RUN easy_install buildbot
RUN buildbot create-master master
RUN mv master/master.cfg.sample master/master.cfg
RUN easy_install buildbot-slave
