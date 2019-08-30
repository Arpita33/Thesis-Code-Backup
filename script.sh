echo "How many taxa do you want to remove?"
read n
#echo "Input the taxa to be removed"
declare -a test_array

counter=1
until [ $counter -gt $n ]
do
#echo $counter
((counter++))
read var
test_array+=$var
done
#echo ${test_array[@]}
for a in "${test_array[@]}"
do
#var=$a
#var+=", "
echo $a
echo ", "
done
