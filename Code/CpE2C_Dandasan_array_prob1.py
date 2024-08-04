from array import array

user_input= array('i', [int(x) for x in input("Input Value (separate with comma): ").split(',')])
print("\nThe Original input: ", *user_input)
print("The Reverse Order: ", *user_input[::-1])
print("The Ascending Order: ", *sorted(user_input))
print("The Decending Order: ", *sorted(user_input, reverse=True))