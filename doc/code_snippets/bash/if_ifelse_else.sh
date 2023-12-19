X=5
Y=10
Z=9

if [ "$X" -eq "$Y" ] && [ "$Z" -eq "$Y" ] && [ "$X" -eq "$Z" ] ; then
  echo "EQUILATERAL"
elif [ "$X" -ne "$Y" ] && [ "$Z" -ne "$Y" ] && [ "$X" -ne "$Z" ] ; then
  echo "SCALENE"
else
  echo "ISOSCELES"
fi

exit 0

if [[ $X > $Y ]]
then
  echo "X is greater than Y"
elif [[ $X < $Y ]]
then
  echo "X is less than Y"
else
  echo "X is equal to Y"
fi
echo $(($X+$Y))
echo $(($X-$Y))
echo $(($X*$Y))
echo $(($X/$Y))


