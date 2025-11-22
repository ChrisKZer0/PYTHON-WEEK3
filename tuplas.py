#Tuple
print("Tuples in Python".upper().center(50))

#Here I put 6 number as requested to the exercise
numbers=(15, 23, 60, 40, 25, 4)
print("\nOriginal tuple:", numbers)

#Frist, If I try to add a value
addedn=numbers+(12,)
print("\n1. If I add a value:", addedn)

#The form that I can to repalace
temp=list(numbers)
temp[2]=80
repladed=tuple(temp)
print("2. If I replace a value:",repladed)

#Now, the form if I delete a value
temp1=list(numbers)
del temp1[4]
deleted=tuple(temp1)
print("3. If I delete a value:", deleted)

#Finally, How I can to show the values with the position
print("\nPosition:\n")
for i in range (len(numbers)):
    print(i, "-", numbers[i])

#Summary about all numbers
print("\n" + "-" * 30)
print("SUMMARY".center(30))
print("-" * 30)

print("\nMax value: ", max(numbers))
print("Min value: ", min(numbers))
print("Sum: ", sum(numbers))
print("Position of max: ", numbers.index(max(numbers)))
print("\n")