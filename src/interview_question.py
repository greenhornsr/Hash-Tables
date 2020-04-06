#Add up and print the sum of the all of the minimum elements of each inner array:
myarray = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# capture the lowest number within each elements array.
# then sum all of the low numbers 

# go through each element in the array, 
# go through each inner element within the element array.
    # store element, compare to next, store lower.
# identify which inner element is lowest, 
# store that inner element value to a new array
# sum that array.  

lowest_nums_array = []

index = 0
sum = 0

for arr in myarray:
    low_num = min(arr)
    print("my low_num: ", low_num)
    lowest_nums_array.insert(index, low_num)
    index += 1

for nums in lowest_nums_array:
    sum += nums
    
print("Total sum:", sum)

#The expected output is given by:
#4 + -1 + 9 + -56 + 201 + 18 = 175

# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.