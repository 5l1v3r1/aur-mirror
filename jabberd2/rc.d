#!/bin/bash

. /etc/rc.conf
. /etc/rc.d/functions

name=jabberd
prog="/usr/bin/jabberd -b"

PID=$(pgrep -f '^perl -w -x /usr/bin/jabberd')

case "$1" in
start)
	stat_busy "Starting $name daemon"
	[[ -z "$PID" ]] && eval $prog &>/dev/null \
	&& { add_daemon $name; stat_done; } \
	|| { stat_fail; exit 1; }
	;;
stop)
	stat_busy "Stopping $name daemon"
	[[ -n "$PID" ]] && kill $PID &>/dev/null \
	&& { rm_daemon $name; stat_done; } \
	|| { stat_fail; exit 1; }
	;;
restart)
	$0 stop
	sleep 2
	$0 start
	;;
*)
	echo "usage: $0 {start|stop|restart|reload}"
	exit 1
	;;
esac
