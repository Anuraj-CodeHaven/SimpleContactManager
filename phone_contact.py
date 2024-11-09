mycontact={"police":100,"ambulance":108,"fireforce":108}
def contact(name:str="anuraj",contact:int=7907011048)->None:
    name=input("enter the  contact name you want to create    ")
    contact=int(input("enter contact  number     "))
    mycontact[name]=contact
    print(name,"is successfully add to the contact ")
    
def delete()->None:
    name=input("enter the  conatct name you want to delete    ")
    mycontact.pop(name)
    print(name,"is successfully deleted in the  contact ")


def display():
    print("all contacts names .if ypu want to get thr number of the contact name .please enter yes otherwise no")
    for i in mycontact:
    	print(i)
    while True:
        choice=input("enter the choice in yes or no only      ")
        if(choice=="yes"):
            name=input("enter the name you want to see the number      ")
            number=mycontact[name]
            print("number of ",name,"is",number)
            break
        elif(choice=="no"):
            print("thank you for choicing this ")
            break
        else:
            print("invalid input .please enter the right one ")

def modify():
    print("what you want to modify the name then enter name or modify number enter number ")
    choice=input("enter the choice ")
    if(choice=="name"):
        name=input("enter the current name    ")
        if name in mycontact:
            u_name=input("enter the new name to update the contact     ")
            temp=mycontact[name]
            mycontact.pop(name)
            mycontact[u_name]=temp
            print("updated successfully")
        else:
            print(name,"it is not exit ")
    elif(choice=="number"):
        name=input("please enter the corresponding name to change the number     ")
        num=int(input("enter the number for update     "))
        mycontact[name]=num
        print("updated successfully")
    else:
        print("enter the valid choice .please enter the right one ")    
            
        
    
    	
    
print("*****MENU*****\n\n1,add a new contact \n2,delete a contact\n3,display all contact \n4,modify the contact \n 5,exit")

while True:
    choice = int(input("Enter your choice:     "))
    match choice:
        case 1:
            contact()
        case 2:
            delete()
        case 3:
            display()
        case 4:
            modify()
        case 5:
            print("Exiting ......")
            break
        case _:
            print("Enter a valid input")
