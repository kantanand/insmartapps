#!/bin/bash
USER="ubuntu"
PIDFILE="/home/ubuntu/learning/learning-uwsgi.pid"

function start(){
    su - ${USER} /bin/sh -c "source /home/ubuntu/env/bin/activate && exec uwsgi --pidfile=${PIDFILE} --master --ini /etc/init.d/learning-uwsgi.ini"
}

function stop(){
    kill -9 `cat ${PIDFILE}`
}

$1
