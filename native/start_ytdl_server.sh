#!/bin/bash
ytdl_server.py > /dev/null 2>&1 &

while ((1)); do
    if pgrep chromium-browse > /dev/null
    then
        #Fine
        echo "HI" > /dev/null
    else
        wget -qO /dev/null http://localhost:9192/stop
        exit 0
    fi
    sleep 20
done
