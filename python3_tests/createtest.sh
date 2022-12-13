#!/usr/bin/env bash
# enables create pytest tasks in vscode in combination with .vscode/tasks.json

if [ $# != 1 ]
then
    echo "Usage: ./createtest.sh question_number"
    exit 1
fi

language=python3
ext=py

number=$1
regex="\.\.\/${language}\/lc_(.+)\.${ext}" # regex to match prolem file name e.g. ../python3/lc_34_easy_stupid_question.py

# check if original question exists first
if name=$(ls ../${language}/lc_${number}_* 2> /dev/null)
then
    if [[ $name =~ $regex ]]
    then
        # match and get file name
        name="${BASH_REMATCH[1]}"
        touch test_${name}.${ext}
        code test_${name}.${ext}
        echo "created test_${name}.${ext}"
    else
        echo "regex didn't match original question file"
        exit 1
    fi
else
    echo "leetcode question not in local repository"
    exit 1
fi