while read lines;
do
    echo $lines # print line
    echo $lines | cut -c3 # print 3rd symbol line
    echo $lines | cut -c3-5 # print from 3rd to 5th symbol line
    echo $lines | cut -c3,5 # print 3rd and 5th symbol line
    echo $lines | cut -c3- # print from 3rd to end
    echo $lines | cut -d' ' -f2
    echo $lines | cut -d',' -f-3
    echo $lines | cut -d',' -f4-
done

# while read lines;
# do
#     f=$(echo $lines | cut -d',' -f-3)
#     s=$(echo $lines | cut -d',' -f4- | cut -d' ' -f1)
#     echo $f,$s
# done


# echo 100.200.300.400 |cut -d '.' -f 1,3
# 100.300
# echo 100.200.300.400 |cut -d '.' -f 1-3
# 100.200.300