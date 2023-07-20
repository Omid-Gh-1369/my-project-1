from array import *
#---------------------
def createArray():
    a = array('i', [])
    n = int(input("Enter the number of array : "))
    i = 1
    while 0<n :
        print("Number", i, ":")
        x = int(input())
        a.append(x)
        n = n-1
        i+=1
    print("Orginal array ")
    printArray(a)
    return a
#---------------------
def printArray(a):
    for i in a:
        print(i, end = '\t')
    print()
#---------------------
def maxArray(a):
    maximum = a[0]
    IMax = 0
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
            IMax = i
    return maximum, IMax

#---------------------
def check_all(a):
    count = 0
    for i in range(len(a)):
        if (a[0] == a[i]):
            count +=1
        else:
            pass
    if count == len(a):
        print("The array has no second smallest!!!")
        return False
    else:
        return True
#---------------------
def secondMin(a):
    check = check_all(a)
    if check == False:
        return False, False
    if len(a)<3:
        if (a[0] < a[1]):
            min1 = a[0]
            min2 = a[1]
            Imin1 = 0
            Imin2 = 1
        else :
            min1 = a[1]
            min2 = a[0]
            Imin1 = 1
            Imin2 = 0
        return min2, Imin2
    else:
        if (a[0] < a[1]):
            min1 = a[0]
            min2 = a[1]
            Imin1 = 0
            Imin2 = 1
        else :
            min1 = a[1]
            min2 = a[0]
            Imin1 = 1
            Imin2 = 0
        for i in range(2,len(a)):
            if (a[i] > min1 and a[i] < min2):
                min1 = min1
                Imin1 = Imin1
                min2 = a[i]
                Imin2 = i
            elif(a[i] < min1 and a[i] < min2):
                min2 = min1
                Imin2 = Imin1
                min1 = a[i]
                Imin1 = i
            else:
                pass

        return min2, Imin2
#-------------------------
def rev_array(a):
    rev_arr = array("i", [])
    rev_arr = a[::-1]
    return rev_arr
# -------------------------
def main():
    a = createArray()
    maximum, IMax = maxArray(a)
    print("Maximum Array Befor Reverse is : ", maximum, "  And Index Maximum is : ",IMax,end="\n")
    min2, Imin2 = secondMin(a)
    if (min2 == False and Imin2 == False):
        pass
    else:
        print("Second Minimum In Array Befor Reverse Is : ", min2, " And Index That Is : ",Imin2,end="\n")
    rev_arr = rev_array(a)
    print("Reverse array :")
    printArray(rev_arr)
    maximum, IMax = maxArray(rev_arr)
    print("Maximum Array After Reverse is : ", maximum, "  And Index Maximum is : ",IMax,end="\n")
    min2,Imin2 = secondMin(rev_arr)
    if (min2 == False and Imin2 == False):
        pass
    else:
        print("Second Minimum In Array After Reverse Is : ", min2, " And Index That Is : ", Imin2, end="\n")
main()
