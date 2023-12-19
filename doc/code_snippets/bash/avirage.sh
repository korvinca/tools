# Read the number of integers
read n

# Initialize sum to zero
sum=0

# Read the integers and add them to the sum
for ((i=0; i<n; i++)); do
    read num
    sum=$((sum + num))
done

# Calculate the average with three decimal places
average=$(echo "scale=3; $sum / $n" | bc)

# Display the result
echo $average