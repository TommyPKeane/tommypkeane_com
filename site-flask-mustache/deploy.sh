#!/bin/sh
# @file
# @brief Deploy script to install flask-based webapp with uwsgi.
#
# @author Tommy P. Keane <talk@tommypkeane.com>
# @copyright 2020, Tommy P. Keane

DEPLOYDIR=./www_deploy


# SYSTEMD SERVICE CONFIGURATION FILE
# ----------------------------------
USERUSER=`id -un`
USERGROUP=`id -gn`
UWSGIAPP=`which uwsgi | sed 's;\/;\\\/;g'`
APPNAME=webapp
APPVARDIR=www
echo ${USERUSER}
echo ${USERGROUP}
echo ${UWSGIAPP}

sed 's/USERUSER/'"$USERUSER"'/g' ${APPNAME}.service |\
   sed 's/USERGROUP/'"$USERGROUP"'/g' |\
   sed 's/UWSGIAPP/'"$UWSGIAPP"'/g' \
   > ${APPNAME}_built.service

cat ${APPNAME}_built.service

sudo -E mv ${APPNAME}_built.service /etc/systemd/system/${APPNAME}.service
# ----------------------------------

# INSTALL CODE
# ----------------------------------
sudo -E cp -r ./${APPVARDIR}/ /var/www
# ----------------------------------


# UWSGI CONFIGURATION FILE
# ----------------------------------
CODEDIR=/var/www/${APPVARDIR}
MODULENAME=www
FLASKAPPALIAS=webapp
SOCKETNAME=webapp.socket

sed 's/CODEDIR/'"$CODEDIR"'/g' ${DEPLOYDIR}/${APPNAME}.ini |\
   sed 's/MODULENAME/'"$MODULENAME"'/g' |\
   sed 's/MODULENAME/'"$MODULENAME"'/g' |\
   sed 's/FLASKAPPALIAS/'"$FLASKAPPALIAS"'/g' \
   > ${DEPLOYDIR}/${APPNAME}_built.service

cat ${DEPLOYDIR}/${APPNAME}_built.service

sudo -E mv ${DEPLOYDIR}/${APPNAME}_built.service /etc/systemd/system/${APPNAME}.service
# ----------------------------------
