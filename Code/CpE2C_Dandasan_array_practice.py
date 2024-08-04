
from array import array


#============= Array declaration =============#

# array1= array('d',[12.3,32.1,44,71.11,12.6])

# for x in array1:
#     print(x)

#========== Accessing Array Elements =============#
# array1= array('d',[12.3, 32.1, 44, 71.11, 12.6])
# print( array1[0], array1[3], array1[4])

#============= Insertion =============#
# array1= array('d',[12.3, 32.1, 44, 71.11, 12.6])
# array1.insert(3, 20)
# array1.insert(3, 30)
# print(array1, end='\n\n')

#============= Deletion =============#
# array1.remove(44)
# array1.remove(20)
# print(array1, end='\n\n')

#============= Search =============#
# print(array1.index(32.1), array1.index(71.11), end='\n\n')

#============= Upadate =============#
# array1= array('d',[12.3, 32.1, 44, 71.11, 12.6])
# array1[0]= 110
# for x in array1:
#     print(x)
# print(" ")

#============= Length if the Array =============#
# print(len(array1), end='\n\n')

#============= Adding Elements =============#
# array1= array('d',[12.3, 32.1, 44, 71.11, 12.6])
# array1.insert(0, 200)
# print(array1)
# array1.append(70.77)
# print(*array1, sep=', ')
# array1.extend([1,2,3,4,5])
# print(*array1, sep=', ', end='\n\n')

#============= Array Concatination =============#
# array2= array1[0:5]
# print('Array Concatination:\n',*(array1+array2), sep=',', end='\n\n')

#============= Slicing Array =============#
# print(*array1, sep=', ')
# print(*array1[1:4], end='\n\n')

#============= Looping through an Array =============#
# for x in array1:
#     print(x)
# print(" ")

#============= Sort an Array =============#
# print(*sorted(array1), sep=', ', end="\n")
# print(*sorted(array1, reverse=True), sep=', ')