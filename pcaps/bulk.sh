#!/bin/bash

declare -a sites=("facebook.com" "twitter.com" "wikipedia.org" "yahoo.com" "amazon.com" "tiktok.com" "linkedin.com" "reddit.com" "netflix.com")

for iter in {1..500}
do 

    for web in "${sites[@]}"
    do

        for i in `seq 1 2`; do
            echo "[$i][$(date)] Capturing $web for $iter iteration..."

            # Start capturing.
            ./capture.sh any $web lynx &

            # Start a lynx session over torsocks.
            torsocks timeout 20 lynx https://$web &

            sleep 20

            # Kill the tcpdump session.
            tcpdump_pid=$(ps axf | grep tcpdump | grep -v grep | awk '{ print $1 }')

            if [[ ! -z $tcpdump_pid ]]; then
                echo "Killing $tcpdump_pid"
                sudo kill -15 $tcpdump_pid
            fi

            # If lynx is still running it needs to be terminated.
            lynx_pid=$(pidof lynx)

            if [[ ! -z $lynx_pid ]]; then
                kill -9 $lynx_pid
            fi
        done

    done

done
