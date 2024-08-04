from array import array



def choice_1(user_array):
    while(True):
        print("--- Enter a value to be append ---")
        user_array.append(int(input("Enter Value: ")))
        print("Choice 1 Output: ", *user_array)
        cont= str(input("\nDo you wish to continue? [y/n] "))
        if (cont == "n"):
            break
    return user_array

def choice_2(user_array):
    while(True):
        print("--- Extend new items or input new values --- ")
        user_array.extend([int(x) for x in input("Enter Values (separate with comma): ").split(',')])
        print("Choice 2 Output: ", *user_array)
        cont= str(input("\nDo you wish to continue? [y/n] "))
        if (cont == "n"):
            break
    return user_array

def choice_3(user_array):
    while(True):
        print("--- Duplicate items will be remove ---") 
        print("Original Array: ", *user_array)
        remo_array = array('l')
        for x in user_array:
            if x not in remo_array:
                remo_array.append(x)
        print("Duplicate Removed: ",*remo_array)
        cont= str(input("\nDo you wish to continue? [y/n] "))
        if (cont == "n"):
            break
    return remo_array

def choice_4(user_array):
    while(True):
        print("--- The End and Last Element of the Array ---")
        print("---> index[",(len(user_array)-1),"]= ", user_array[(len(user_array)-1)], sep='')
        cont= str(input("\nDo you wish to continue? [y/n] "))
        if (cont == "n"):
            break
    return user_array

def chioce_5(user_array):
    while(True):
        print("--- Enter a number to be inserted in the middle of the array ---")
        mid_num= int(input("Enter: "))
        user_array.insert(int(len(user_array)/2), mid_num)
        print("Choice 5 Output: ", *user_array)
        cont= str(input("\nDo you wish to continue? [y/n] "))
        if (cont == "n"):
            break
    return user_array

user_array= array('i',[int(x) for x in input("Enter array numbers (separate with comma): ").split(",")])
while(True):
    print("\n\nPress 1 - Append new item and then print", "Press 2 - Extend new items and then print", \
        "Press 3 - Remove the duplicate items and then print", "Press 4 - Print the end and last element of the array", \
        "Press 5 - Enter a number to be insert in the middle of array and then print","Press 6 - EXIT", sep="\n")
    choice= int(input("Enter: "))

    if (choice==1):
        user_array = choice_1(user_array)
    elif (choice==2):
        user_array = choice_2(user_array)
    elif (choice==3):
        user_array = choice_3(user_array)
    elif (choice == 4):
        user_array = choice_4(user_array)
    elif (choice == 5):
        user_array = chioce_5(user_array)
    elif (choice == 6):
        print("Thank you for using!")
        break
    else: continue


     
