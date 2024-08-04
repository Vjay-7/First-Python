
operator=['+','-','/','*','^','(',')']
precedenceVal= {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(':4, ')':4}  


# ----------->  Problem 1  <----------- #
def infix_to_postfix(infix):
    oprt, oprnd, finalOutput=[],[],[]                   
    for x in infix:
        if x in operator:
            if (oprt==[]): oprt.append(x)
            elif (precedenceVal.get(x)<precedenceVal.get(oprt[len(oprt)-1])):
                for z in range(len(oprt)):
                    oprnd.append(oprt.pop())
                oprt.append(x)
            else: oprt.append(x)
        else:
            oprnd.append(x)
    finalOutput= oprnd+oprt[::-1]
    print('INFIX to POSTFIX -->',*finalOutput)

# ----------->  Problem 2  <----------- #
def infix_to_prefix(infix):
    infix.reverse()
    oprt, oprnd, finalOutput=[],[],[]
    for x in infix:
        if x in operator:
            if (oprt==[]): oprt.append(x)
            elif (precedenceVal.get(x)<precedenceVal.get(oprt[len(oprt)-1])):
                for z in range(len(oprt)):
                    oprnd.append(oprt.pop())
                oprt.append(x)
            else: oprt.append(x)
        else:
            oprnd.append(x)
    finalOutput= oprnd+oprt
    finalOutput.reverse()
    print('INFIX to PREFIX -->',*finalOutput)


# ----------->  Problem 3  <----------- #
def evalPostfix():
    evalinfix=[str(x) for x in input("\n\nEnter INTEGER Expression separate with space: ").split(' ')]
    finalOutput=[]
    for x in evalinfix:
     if x in operator:
         simp=[]
         simps=' '
         simp.append(finalOutput.pop((len(finalOutput)-2)))
         simp.append(x)
         simp.append(finalOutput.pop((len(finalOutput)-1)))
         finalOutput.append(str(eval(simps.join(simp))))
     else:
         finalOutput.append(x)
    print('---> Answer: ',*finalOutput)

while(True):
    print("\n\nPress 1 - Convert INFIX to POSTFIX Notation (Problem 1)\n" 
              "Press 2 - Convert INFIX to PREFIX Notation (Problem 2)\n"
              "Press 3 - EVALUATE a POSTFIX Notation [Input Integers] (Problem 3)\n"
              "Press 4 - EXIT")
    choice= int(input("Enter: "))
    
    if (choice==1): 
        infix= [str(x) for x in input("\n\nEnter Expression separate with space: ").split(' ')]
        infix_to_postfix(infix)
    elif (choice==2):
        infix= [str(x) for x in input("\n\nEnter Expression separate with space: ").split(' ')]
        infix_to_prefix(infix)
    elif (choice==3): evalPostfix()
    else: break