#!/bin/bash

#Anthony Androulakis, 2019

#this script runs racotuge, the Random & Constrained Tune Generator! :)
#to run this specific script write ./racotuge.sh 100 in the terminal in the 
#racotuge directory to get 100 tunes.

num=$1
racotuge(){
    python3 -c 'from run import maketune; maketune('$num')'
    cd tunes
    cd mid
    for i in * 
    do
        if test -f "$i" 
        then
	    echo $i
            '/Applications/MuseScore 3.app/Contents/MacOS/mscore' -o ../wav/${i::${#i}-4}.wav $i
        fi
    done
}

racotuge $num
