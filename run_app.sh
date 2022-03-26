#!/bin/bash

test=0
while [[ $# -gt 0 ]]; do
    case $1 in 
    -h|--host)
        HOST=$2
        shift # past arguement
        shift # past value
        ;;
    -p|--port)
        PORT=$2
        shift # past arguement
        shift # past value
        ;;
    esac 
done

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
    echo "$HOST/$PORT"
    service postgresql start
    startApp
    until $(curl --output /dev/null --silent --head --fail "$HOST:$PORT/ready"); do 
        note ".$NC"
        sleep 3
    
    done

    read -p $(note "Press any key to stop the app... \n") -n1 -s

    bash shutdown_app.sh
    
}



main 


