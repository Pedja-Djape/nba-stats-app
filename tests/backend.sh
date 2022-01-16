#!/bin/bash


function hitEndpoint {
    host="$1"
    endpoint="$2"

    curl "$host/$endpoint"
}

hitEndpoint "$1" "$2"