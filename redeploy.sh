#!/bin/sh
# @file
# @brief Redeployment script to update flask-based webapp with uwsgi.
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

# VARIABLES
# ----------------------------------
USERUSER=`id -un`
USERGROUP=`id -gn`
UWSGIAPP=`which uwsgi | sed 's;\/;\\\/;g'`
DEPLOYDIR=/var/www
APPNAME=webapp
APPVARDIR=www
echo ${USERUSER}
echo ${USERGROUP}
echo ${UWSGIAPP}
# ----------------------------------

# GET AND MOVE CODE
# ----------------------------------
git pull;
sudo -E cp -r ./${APPVARDIR}/ ${DEPLOYDIR};
sudo -E chown -R ${USERUSER}:${USERGROUP} ${DEPLOYDIR}/${APPVARDIR};
# ----------------------------------

# RESTART SERVICES
# ----------------------------------
sudo -E systemctl restart ${APPNAME};
sudo -E nginx -s reload;
# ----------------------------------
