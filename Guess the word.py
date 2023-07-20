import random
#-----------------------------------------------
def check_char(char, Random_Name, temp):
    boll = True
    while boll :
        if char in Random_Name:
            indix = Random_Name.find(char)
            removed_character ='*'
            Random_Name = Random_Name[:indix]+removed_character+Random_Name[indix+1:]
            temp[indix] = char
        else:
            boll = False
    return (Random_Name, temp)
#-----------------------------------------------
def win_check():
    for i in range(0, len(temp)):
        if temp[i] == '_':
            return False
    return True
#-----------------------------------------------
def Receive_names():
    list_name = []
    names = input("Please enter a list of names : ")
    list_name = names.split(" ")
    Random_Name = random.choice(list_name)
    return (Random_Name)
#-----------------------------------------------
Random_Name = Receive_names()    
name = Random_Name
temp = ['_']* len(Random_Name)
print("Random name is : ", temp)
num_loops = len(Random_Name)
for i in range(num_loops+1):
    num_loops
    char = input('Guess a character : ')
    if char in Random_Name:
        Random_Name, temp = check_char(char, Random_Name, temp)
        print("The letter is in word.")
        print(temp)
    else:
        print(temp)
        print('Sorry that letter is not in the word.')
        print('you have '+str(num_loops-i)+' turns left.') 
    if win_check() == 1:
        print('\n')
        print("""*** you won ***
The name is : """, name)
        break    
    print()

