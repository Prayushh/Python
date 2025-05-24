#to find largest number in a list
list=[2,9,5,1,6]
largest=list[0]
for item in list:
    if item>largest:
        largest=item
print(largest)