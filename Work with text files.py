import fileinput
import  os
#--------------------------
def Show_File(text):
    if len(text) == 0:
        print("File is empty")
    else:
        for line in text:
            print(line)
#--------------------------
def Create_File():
    Add = input("Enter address file...    for example: 'D://Ta' : ")
    name = input("please enter name for file : ")
    try:
        file = open(Add + "/" + name + ".txt" , "x")
        print("Successful")
    except:
        print("Something went wrong when create the file!!!")
    finally:
        file.close()
#--------------------------
def Read_File():
    Add = input("Enter address file...    for example: 'D://Ta' : ")
    name = input("please enter name of file for reading : ")
    if os.path.exists("D://" + name + ".txt"):
        try:
            file = open(Add + "/" + name + ".txt", "r+")
            text = file.readlines()
            Show_File(text)
        except:
            print("Something went wrong when read the file or file not found !!!")
        finally:
            file.close()
    else:
        print("File is not found!!!")
#--------------------------
def Write_File():
    boll = True
    while(boll):
        Add = input("Enter address file...    for example: 'D://Ta' : ")
        name = input("please enter name of file for writing : ")
        if os.path.exists(Add + "/" + name + ".txt"):
            print("""please select : 1.writing to end file
                    2.replace text
                    """)
            type = int(input("only the number of selsection : "))
            try:
                if type == 1:
                    try:

                        file = open(Add + "/" + name + ".txt", "a")

                        str = input("enter a text for writing : ")
                        file.write(str)
                    except:
                        print("Something went wrong when write into the file !!!")
                    finally:
                        file.close()
                        boll = False
                elif type == 2:
                    try:
                        file = open(Add + "/" + name + ".txt", "w")
                        str = input("enter a text for writing to append : ")
                        file.write(str)
                    except:
                        print("Something went wrong when write into the file!!!")
                    finally:
                        file.close()
                        boll = False
            except:
                print("wrong input")
        else:
            print("File is not found!!!")
#--------------------------
def Search_File():
    Add = input("Enter address file...    for example: 'D://Ta' : ")
    name = input("please enter name of file : ")
    if os.path.exists(Add + "/" + name + ".txt"):
        search_text = input("Enter the word you want to search in the file : ")
        try:
            file = open(Add +"/" + name + ".txt", "r")
            text = file.readlines()
            for line in text:
                if search_text in line:
                    print("Founded")
                else:
                    print("Not found")
            file.close()
        except:
            print("Something went wrong when read the file or not file founded!!!")
    else:
        print("File is not found!!!")
#--------------------------
def Edit_File():
    Add = input("Enter address file...    for example: 'D://Ta' : ")
    name = input("please enter name of file for writing : ")
    if os.path.exists(Add +"/" + name + ".txt"):
        search_text = input("Enter the word you want to edit in the file : ")
        replace_text = input("Enter the new word you want to replace in the file : ")
        try:
            fin = open(Add +"/" + name + ".txt", "rt")
            data = fin.read()
            data = data.replace(search_text, replace_text)
            fin.close()
            fout = open(Add +"/" + name + ".txt", "wt")
            fout.write(data)
            fout.close()
        except:
            print("Something went wrong when read or write into the file or not file founded!!!")
    else:
        print("File is not found!!!")
#--------------------------
def Delete_File():
    Add = input("Enter address file...    for example: 'D://Ta' : ")
    name = input("name of file for delete : ")
    try:
        os.remove(Add +"/" + name + ".txt")
        print("File deleted")
    except:
        print("File not found!!!")
#--------------------------
def default():
    print("Wrong input!!!")
#--------------------------
switcher = {
    1: Create_File,
    2: Read_File,
    3: Write_File,
    4: Search_File,
    5: Edit_File,
    6: Delete_File
    }
#--------------------------
def switch(key):
    x = switcher.get(key, default)()
#--------------------------
boll1=True
while(boll1):
    print("""        1: Create
        2: Read
        3: Write
        4: Search
        5: Edit
        6: Delete
        7: Exit
        """)
    key = int(input("Select number of list items : "))
    if key == 7:
        print("Exit")
        exit()
    switch(key)
