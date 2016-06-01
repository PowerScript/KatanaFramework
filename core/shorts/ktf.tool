#!/bin/bash
PARAMETERS=""
while (( $# > 0 ))   
do
    PARAMETERS+=" "$1
    shift
done
cd /usr/share/KatanaFramework
sudo python ktf.tool $PARAMETERS
