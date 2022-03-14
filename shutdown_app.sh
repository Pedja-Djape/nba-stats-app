#!/bin/bash

function shutdownApp {
    app_processes=$(ps -ef | grep -e postgres -e 'nba-stats' | awk '{print $2}')
    for pid in $app_processes; do 
        kill -9 $pid;
    done

    app_processes=$(ps -ef | grep -e postgres -e 'nba-stats' | awk '{print $2}')
    if [[ -z "$app_processes" ]]; then
        echo "ALL APP PROCESSES KILLED!"
    fi
}

shutdownApp