#!/bin/bash

write_log() {
	while read text
	do 
		LOGTIME=`date "+%Y-%m-%d %H:%M:%S"`
		LOG=$1
		touch $LOG
		if [ ! -f $LOG ]
		then 
			echo "ERROR!! Cannot create log file $LOG. Exiting." 
			exit 1
		fi
		echo $LOGTIME": $text" | tee -a $LOG;
	done
}

## Ensure running setup as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

## Create Log File Path
mkdir -p "`pwd`/logs/setup_cstk"
LOG_FILE="`pwd`/logs/setup_cstk/`date '+%Y%m%d_%H%M%S'`_setup.log"

## Run installed_pkg_checks.sh to check installs
./installed_pkg_checks.sh | write_log $LOG_FILE

## Create a virtual env
virtualenv -p /usr/bin/python3 venv | write_log $LOG_FILE
source venv/bin/activate 

## Install python packages based on requirements.txt
cat requirements.txt | xargs -n 1 pip install | write_log $LOG_FILE

## Complile and Install netifaces
pushd special_installs/netifaces
echo "y" | ../../venv/bin/python setup.py install | write_log $LOG_FILE
popd

python create_env.py

python manage.py makemigrations --noinput
python manage.py migrate --noinput