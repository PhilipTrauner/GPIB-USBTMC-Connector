#!/usr/bin/python

import os
import Modules.TermOut.Logging as Logging

Logging.header("This is going to take a while and needs a stable internet connection. Continue? [ENTER]")
raw_input()
Logging.header("Updating package index")
os.system("sudo apt-get update")
os.system("sudo apt-get -y upgrade")
Logging.success("Package index up-to-date")
Logging.header("Fetching required packages")
os.system("sudo apt-get -y install linux-headers-$(uname -r) usbutils build-essential make gcc python kernel-package texinfo texi2html libcwidget-dev libncurses5-dev libx11-dev binutils-dev bison flex libusb-1.0-0 libusb-dev libmpfr-dev libexpat1-dev tofrodos subversion autoconf automake libtool python-dev python2.7-dev fxload build-essential bzip2 libbz2-dev sqlite3 libsqlite3-dev libssl-dev git")
Logging.success("All required packages have been downloaded")
Logging.header("Installing linux-gpib")
os.chdir("Libs/")
os.system("tar xf linux-gpib-4.0-rc1.tar.gz")
os.system("rm linux-gpib-4.0-rc1.tar.gz")
os.chdir("linux-gpib-4.0-rc1")
os.system("./configure")
os.system("make")
os.system("sudo make install")
os.system("sudo adduser $USER gpib")
os.system("sudo ldconfig")
os.chdir("..")
Logging.header("Installing pyusb")
os.system("git clone https://github.com/walac/pyusb")
os.chdir("pyusb")
os.system("sudo python setup.py install")
os.chdir("..")
Logging.header("Installing usbtmc")
os.system("git clone https://github.com/python-ivi/python-usbtmc")
os.chdir("python-usbtmc")
os.system("sudo python setup.py install")
os.chdir("..")
Logging.header("Loading kernel modules")
os.system("sudo modprobe hp_82341 agilent_82350b agilent_82357a cec_gpib tnt4882 ines_gpib hp82335 ni_usb_gpib")
Logging.success("Installation of linux-gpib successful")
Logging.header("Compiling tool to reset usb connections")
os.system("gcc -o usbreset usbreset.c")
Logging.success("Finished compiling usb tool")
os.system("sudo mv usbreset /usr/bin/")
Logging.success("Installation complete!")
Logging.header("A reboot is required in order to use linux gpib. Continue? [ENTER] (^C to reboot later)")
raw_input()
os.system("sudo reboot")