#!/usr/bin/env bash
readarray -t my_array </dev/stdin
# Input array is read and stored in to my_array variable. 
# You can view the code by pressing > button above. 

count=1
res=""
for i in $my_array
do
    echo $i
    if [[ count > 3 ]]
        echo $i" " >> res
    fi
    count = $((count + 1))
done

exit 0