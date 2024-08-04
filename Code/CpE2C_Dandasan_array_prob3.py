
from array import array

print('Enter a array of numbers range from 30-40')

user_array= array('i',[int(inp) for inp in input("Enter numbers (separate with comma): ").split(',')])
for x in user_array:
    if(x>40 or x<30):
        print("Incorrect Range! Please input numbers between 30-40")
        exit()
print("\nOriginal Input Array: ", *user_array)
missing_num= array('i', [])
for x in range(30,41):
    if  x not in user_array:
        missing_num.append(x)

print("Missing numbers (30-40): ", *missing_num)