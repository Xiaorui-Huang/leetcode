#!/bin/bash
# enables create pytest tasks in vscode in combination with .vscode/tasks.json

if [ $# != 1 ]
then
    echo "Usage: ./createtest.sh question_number"
    exit 1
fi

number=$1
regex="\.\.\/python3\/lc_(.+)\.py" # regex to match prolem file name e.g. ../python3/lc_34_easy_stupid_question.py

# check if original question exists first
if name=$(ls ../python3/lc_${number}_* 2> /dev/null)
then
    if [[ $name =~ $regex ]]
    then
        # match and get file name
        name="${BASH_REMATCH[1]}"
        touch test_${name}.py
        code test_${name}.py
        echo "created test_${name}.py"
    else
        echo "regex didn't match original question file"
        exit 1
    fi
else
    echo "leetcode question not in local repository"
    exit 1
fi