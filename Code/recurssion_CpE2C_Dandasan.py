
# //////////////////////////////////////////////////
# #Recursion
# /////////////////////////////////////////////////

def sum_calc(num):
    if not num:     #---------> This is the base case, it return 0 if the data inside the num list is empty
        return 0
    return num[0] + sum_calc(num[1:])  #------> Using the slicing operation in list we take the indivudual return and sum it up until it meet the base case that return zero

#This statement is to get the user input numbers by spaces using list comprehension and split function by comma
num= [int(item) for item in input("Enter values (separate with comma) : ").split(',')]

#Print the sum_calc recursive function
print(sum_calc(num))
