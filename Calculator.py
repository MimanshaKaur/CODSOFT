choice=0
while(choice==0):
    a=int(input("Enter First Number: "))
    b=int(input("Enter Second Number: "))
    print("<-----CHOOSE THE OPERATOR TO PERFORM FOLLOWING OPERATIONS----->")
    print("(+) ---> FOR ADDITION")
    print("(-) ---> FOR SUBTRACTION")
    print("(*) ---> FOR MULTIPLICATION")
    print("(/) ---> FOR DIVISION")
    o=input("ENTER THE OPERATOR :")
    if(o=='+'):
        print("RESULT= ",a+b)
    elif(o=='-'):
        print("RESULT= ",a-b)
    elif(o=='*'):
        print("RESULT= ",a*b)
    elif(o=='/'):
        print("RESULT= ",a/b)
    else:
        print("INVALID CHOICE !!!")
    print("Do You Want To Continue?")
    c=input("Enter YES/NO : ")
    if(c=="YES" or c=="yes"):
        choice=0
    else:
        choice=1