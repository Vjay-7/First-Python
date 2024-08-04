


# /////////////////////////////////////////////////////
# 1 # Type Conversion
# /////////////////////////////////////////////////////

# pets= ['Minggoy','Dongdong','Mingmong','Moymoy','Nanay','Kakang']
# pets= tuple(pets)
# print(pets)
# print(type(pets))

# grades= [['Math', 90],['English', 91],['Science',92]]
# print(dict(grades))
# print(grades[0])

# num1= 156
# num2= 1.23
# sum_num= num1 + num2 
# print(sum_num)


# /////////////////////////////////////////////////////
# 2 #Input, Output, Import
# /////////////////////////////////////////////////////

# from datetime import datetime
# print("Birthday", "Information", sep=("_"))
# mon = input("Enter Month: ")
# day= input("Enter day: ")
# year= input("Enter year: ")
# print("/nYour birthday is on", mon, day, year )
# print('This information recorded on ',datetime.now() )


# ////////////////////////////////////////////////////////
# 3# Operators
# ////////////////////////////////////////////////////////
# num1= 123; num2=100; num3= 321
# n1, n2, n3= 3, 2, 4 
# print(num1+num2+num3)
# print(num1/num2-num3)
# print(num2%n2, n3**n2, num2*n3, sep=" <=> ")

# num= 1243.345678
# num1 = 6.45
# num3= 1567.5867
# print('%3.2f' %num3)
# print('%1.2f' %num,'%2.2f' %num, '%9.4f' %num,'sa decimal %5.4f' %num, sep=" <=> ")
# print('If ato i round of man galeh', round(num+num1))


# ///////////////////////////////////////////////////////////
# 4# If-Else Statements
# ///////////////////////////////////////////////////////////
# passw= input("Enter password: ")
# if passw == 'Batman':
#     code= int(input('Enter Code: '))
#     if code == 6073:
#         print("~ Welcome to the Batcave ~")
#     else: print('Second Security Denied!')
# else: print('Access Denied')    



# /////////////////////////////////////////////////////////////
# 5# Loops
# //////////////////////////////////////////////////////////////

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print("")


# start = int(input("Start: "))
# end = int(input("End: "))
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# ////////////////////////////////////////////////////////////////////
# 6# Function
# ////////////////////////////////////////////////////////////////////

# def info(name, age):
#     print('My name is', name, 'I am', age, 'years old')

# info(input('Name: '), input('Age: '))

# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0

# print(addition(int(input('Enter value: '))))
