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
    python3 wsgi.py &
}

function main {
    host="$1"
    port="$2"

    service postgresql start
    startApp
    until $(curl --output /dev/null --silent --head --fail "$host:$port/ready"); do 
        note ".$NC"
        sleep 3
    
    done

    read -p $(note "Press any key to stop the app... \n") -n1 -s
    bash shutdown_app.sh
    
}

main "http://127.0.0.1" "5000"


