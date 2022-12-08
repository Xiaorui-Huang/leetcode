#!/bin/bash

if [ $# != 1 ]
then
    echo "Usage: ./createtest.sh question_number"
    exit 1
fi

number=$1
regex="\.\.\/python3\/lc_(.+)\.py"

if name=$(ls ../python3/lc_${number}_* 2> /dev/null)
then
    if [[ $name =~ $regex ]]
    then
        name="${BASH_REMATCH[1]}"
        touch test_${name}.py
        echo "created test_${name}.py"
    else
        echo "didn't match"
    fi
fi

