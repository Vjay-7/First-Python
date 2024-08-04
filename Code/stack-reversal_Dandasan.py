

def create_stack(): 
    stack = [str(x) for x in input("\n\nEnter Character: ")] 
    return stack

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
    if(check_empty(stack)): 
        return "stack is empty"
    return stack.pop()

def printStack(stack):
    for x in stack:
        print(x)

def reverseChar(character):
    revchar=[]
    for x in range(len(character)):
        revchar.append(pop(character))
    return revchar 


characterStack= create_stack()
print("Input: ")
printStack(characterStack)
print("\nOutput: ")
printStack(reverseChar(characterStack))


















# character= [str(x) for x in input("\n\nEnter Character: ")]        # All characters input store in the character list
# print("Input: ")
# for x in character:                                                # Display all inputs by character in the character list
#     print(x)    
# stackChar= []                                                      # A list for the stack to be store
# for x in range(len(character)):
#     revereseChar.append(character.pop())                           # All the characters that pop() from the character list is append to the stackChar list
# print("\nOutput: ")
# for x in stackChar:                                                # It individually print all the character inside the stackchar list
#     print(x)
