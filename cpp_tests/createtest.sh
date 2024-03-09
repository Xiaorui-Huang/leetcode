#!/usr/bin/env bash
# enables create pytest tasks in vscode in combination with .vscode/tasks.json

if [ $# != 1 ]; then
    echo "Usage: ./createtest.sh question_number"
    exit 1
fi

language=cpp
ext=cpp

number=$1
regex="\.\.\/${language}\/lc_(.+)\.${ext}" # regex to match prolem file name e.g. ../python3/lc_34_easy_stupid_question.py

# check if original question exists first
if filepath=$(ls ../${language}/lc_${number}_* 2>/dev/null); then
    if [[ $filepath =~ $regex ]]; then
        # match and get file name
        name="${BASH_REMATCH[1]}"
        testfile=test_${name}.${ext}
        touch ${testfile}
        # code ${testfile}
        echo "created ${testfile}"

        # ==== cpp specific header files ====
        # append include header to .cpp file
        file=lc_${name}.cpp
        echo "#include <gtest/gtest.h>" >>$testfile
        echo "#include \"${file}\"" >>$testfile

        echo "
TEST(LeetCode, $lc_${name}) {
    auto sol = Solution();
    // EXPECT_EQ(sol.<function>(*args), <expected>);
}" >> $testfile

        # wrap header file in header guard
        (echo "#define $(echo lc_${name} | tr '[:lower:]' '[:upper:]')_H" && cat $filepath) >temp && mv temp $filepath
        (echo "#ifndef $(echo lc_${name} | tr '[:lower:]' '[:upper:]')_H" && cat $filepath) >temp && mv temp $filepath
        echo "#endif" >>$filepath

    else
        echo "regex didn't match original question file"
        exit 1
    fi
else
    echo "leetcode question not in local repository"
    exit 1
fi
