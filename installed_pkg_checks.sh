#!/bin/bash

## bash function to escape install_check args
awk_escape () {
	awk '/\install/{print $1}'
}

## bash function to check if item is installed and installs it if not there
install_check () {
	PKG_TO_CHECK=$1
	PKG_INSTALLED=$(dpkg --get-selections | awk_escape | grep -wx "\b$PKG_TO_CHECK\b")

	while [ "$PKG_INSTALLED" != "$PKG_TO_CHECK" ]
	do
		echo "Need to install $PKG_TO_CHECK, attempting to install";
		echo "PKG_INSTALLED returns $PKG_INSTALLED";
		apt-get -qq install $PKG_TO_CHECK;
		PKG_INSTALLED=$(dpkg --get-selections | awk_escape | grep -wx "\b$PKG_TO_CHECK\b");
	done
}

## bash function to check if item is installed and installs it if not there while ignoreing prompts (needed for wireshark)
install_interactive () {
	PKG_TO_CHECK=$1
	PKG_INSTALLED=$(dpkg --get-selections | awk_escape | grep -wx "\b$PKG_TO_CHECK\b")

	while [ "$PKG_INSTALLED" != "$PKG_TO_CHECK" ]
	do
		echo "Need to install $PKG_TO_CHECK, attempting to install";
		echo "PKG_INSTALLED returns $PKG_INSTALLED";
		DEBIAN_FRONTEND=noninteractive apt-get -qq install $PKG_TO_CHECK;
		PKG_INSTALLED=$(dpkg --get-selections | awk_escape | grep -wx "\b$PKG_TO_CHECK\b");
	done
}

install_check "python3"
install_check "python3-dev"
install_check "virtualenv"
install_check "python3-virtualenv"
install_check "tcpdump"
install_interactive "wireshark"
install_check "rabbitmq-server"
install_check "git"
install_check "kismet"
install_check "bluez" 
install_check "bluez-test-scripts" 
install_check "python-bluez"
install_check "python-dbus"
install_check "libsqlite3-dev" 
install_check "ubertooth"
