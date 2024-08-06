#!/bin/sh

pidfile=/var/run/nginx.pid
logdir=/var/log/nginx

if [ -f "$pidfile" ]; then
    echo "rotating nginx logs"
    for logfile in access error; do
        mv ${logdir}/${logfile}.log ${logdir}/${logfile}.log.old
    done

    kill -HUP $(cat "$pidfile")
fi