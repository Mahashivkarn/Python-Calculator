# Python Claculator Using Matchcase
a =int(input("Enter 1st number\n")) #Input of 2 Numbers
b =int(input("Enter 2nd number\n"))

calc=input("What do u want +,_,*,/ \n") #Deciding What Opertion to perform

match calc:
    case "+":
        print("Addition:",a+b)
    case "-":
        print("Subtaction",a-b)
    case"*":
        print("Multiplaction",a*b)
    case"/":
        if(b!=0):
            print("Division",a/b)
        else:
            print("Cannot be divisabe by 0")
            
    case _:
        print("Invalid Operator.")  