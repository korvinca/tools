x=1
while [ $x -le 100 ]
do
    # if [ $((x%2)) -eq 0 ] ; then
    if [ $((x%2)) -ne 0 ] ; then
        echo $x
    fi
    x=$(( $x + 1 ))
done