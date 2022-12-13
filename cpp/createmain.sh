#!/usr/bin/env bash

if [ $# != 1 ]
then
    echo "Usage: ./createmain.sh question_number"
    exit 1
fi


entry_point_folder=mains
number=$1
regex="lc_(.+)\.cpp" # regex to match prolem file name e.g. lc_34_easy_stupid_question.cpp


if name=$(ls lc_${number}_* 2> /dev/null)
then
    if [[ $name =~ $regex ]]
    then
        # match and get file name
        name="${BASH_REMATCH[1]}"
        main_file=${entry_point_folder}/main_${name}.cpp
        touch $main_file
        echo "#include \"lc_${name}.cpp\"" > $main_file
        echo $main_file
        code $main_file
        echo "created main_${name}.cpp"
    else
        echo "regex didn't match original question file"
        exit 1
    fi
else
    echo "leetcode question not in local repository"
    exit 1
fi