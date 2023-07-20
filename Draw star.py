
def Show_Star_Left(n):
    for i in range(1 , n+1 , 2):
        for j in range(i):
             print("*" , end = "")
        print()
#--------------------------
def Show_Star_Center(n):
    for i in range(1 , n+1 , 2):
        for j in range(n+((n//2)-i)//2):
            print(" " , end = "")
        for k in range(i):
            print("*" , end = "")
        print()
#--------------------------
def Show_Star_Right(n):
    for i in range(1 , n+1 ,2):
        for j in range((n*2+(n//2)-i)):
            print(" " , end = "")
        for k in range(i):
            print("*" , end = "")
        print()
#--------------------------
def Select(arange,inputt):
    if arange == 1:
        Show_Star_Left(inputt)
    elif arange == 2:
        Show_Star_Center(inputt)
    elif arange == 3 :
        Show_Star_Right(inputt)
    else:
        print("Wrong Input")
#--------------------------
if __name__ == '__main__':
    inputt = int(input("Enter the number of stars : "))
    print("""1.Left
2.Center
3.Right""")
    arange = int(input("Please select the arrange format : "))
    Select(arange,inputt)


