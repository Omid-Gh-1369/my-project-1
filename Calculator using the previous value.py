def AddNumber(num1, num2):
    add = num1 + num2
    return add
#--------------------------
def MinNumber(num1, num2):
    mine = num1 - num2
    return mine
#--------------------------
def MulNumber(num1, num2):
    mul = num1 * num2
    return mul
#--------------------------
def DivNumber(num1, num2):
    if num2==0:
        return ("Can't divide by zero")
    else:
        div = num1 / num2
        return div
#--------------------------
def GetNumber():
    num1 = float(input("Enter number 1: "))
    while(True):
        oper = input("Please Select One between '+' , '-' , '*' , '/' : ")
        if oper not in ["*" , "+" , "/" , "-"]:
            print('Wrong input')
        else:
            break
    num2 = float(input("Enter number 2: "))
    if(oper == '+'):
        result = AddNumber(num1, num2)
        print("result is : " , result)
        return result
    elif(oper == '-'):
        result = MinNumber(num1, num2)
        print("result is : " , result)
        return result
    elif(oper == '*'):
        result = MulNumber(num1, num2)
        print("result is : " , result)
        return result
    else:
        result = DivNumber(num1, num2)
        print("result is : " , result)
        return result
#--------------------------
def continu(num):
    num1 = num
    print ("The result of previous calculations : ", num1)
    while(True):
        oper = input("Please Select One between '+' , '-' , '*' , '/' : ")
        if oper not in ["*" , "+" , "/" , "-"]:
            print('Wrong input')
        else:
            break
    num2 = float(input("Enter new number : "))
    if(oper == '+'):
        result = AddNumber(num1, num2)
        print("result is : " , result)
        return result
    elif(oper == '-'):
        result = MinNumber(num1, num2)
        print("result is : " , result)
        return result
    elif(oper == '*'):
        result = MulNumber(num1, num2)
        print("result is : " , result)
        return result
    else:
        result = DivNumber(num1, num2)
        print("result is : " , result)
        return result
#--------------------------
if __name__=="__main__":
    result=GetNumber()
    while (True):
        step1 = input("Do you want to continue? 'y' for Yes and 'n' for No:    ")
        if step1 == ('y'):
            step2 = input("Do you want to continue the previous calculations? 'y' for Yes and 'n' for No:    ")
            if step2 == ('y'):
                if result=="Can't divide by zero":
                    print("""previous calculations is wrong!
please enter two new number ... """)
                    result = GetNumber()
                else:
                    result = continu(result)
            else:
                result = GetNumber()
        elif step1 == ('n' or "N"):
            print("Exit")
            exit()
        else:
            print("Wrong input!!!")
    exit()
