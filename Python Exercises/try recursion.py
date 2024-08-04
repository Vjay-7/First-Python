


def sum_calc(index):
    if index == 0:     #---------> This is the base case, it return 0 if the data inside the num list is empty
        return 0
    return sum_calc(index) + sum_calc(index-1)  #------> U

#This statement is to get the user input numbers by spaces using list comprehension and split function by comma
num= [int(item) for item in input("Enter values (separate with comma) : ").split(',')]
index= len(num)
#Print the sum_calc recursive function
print(index)