#!/bin/bash

NC='\033[0m'
RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'

function note {
    echo -e "${BLUE} $1 ${NC}"
}
function error {
    echo -e "${RED} $1 ${NC}"
}
function success {
    echo -e "${GREEN} $1 ${NC}"
}

function startApp {
    source venv/bin/activate
    flask run &
}

function shutdownApp {
    for pid in $(ps -ef | grep "nba-stats" | awk '{print $2}'); do 
        kill -9 $pid; done
}

function main {
    host="$1"
    port="$2"
    cd ..
    startApp
    until $(curl --output /dev/null --silent --head --fail "$host:$port/ready"); do 
        printf "."
        sleep 3
    done
    cd ./tests
    note "TESTING BACKEND"
    ./backend.sh "$host:$port" "api/shotchart/player/201565"
    shutdownApp
}


main "http://127.0.0.1" "5000"


