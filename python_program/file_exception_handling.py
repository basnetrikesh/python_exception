import os,sys #these module is for the path of the file
#function to create a file
def createFile():
    try:
        f=open(os.path.join(sys.path[0],"dataFile.txt"),"w")
        print("dataFile.txt file sucessfully created")
        f.close()
    except:
        print("Error occured while creating the file")
    input() #this is to pause until key is pressed
    mainMenu()

#function to enter data
def enterData():
    try:
        f=open(os.path.join(sys.path[0],"dataFile.txt"),"a")
        while True:
            d=input("enter any data you want:")
            f.write(d+"\n")
            ch=input("do you want to store another data?[Y/N]:")
            if ch=='N' or ch=='n':
                break
        f.close()
    except:
        print("Error occured while openning the file named dataFile.txt")
    input()
    mainMenu()

        
#this function is to view the data stored in the file
def viewData():
    print("Data inside the file:")
    try:
        f=open(os.path.join(sys.path[0],"dataFile.txt"),"r")
        print("")
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("dataFile.txt file doesnot found")
    except FileExistsError:
        print("dataFile.txt file doesnot found")
    input()
    mainMenu()


#function to delete file
def deleteFile():
    try:
        os.remove(os.path.join(sys.path[0],"dataFile.txt"))
        print("dataFile.txt is deleted")
    except FileNotFoundError:
        print("dataFile.txt File doesnot found")
    input()
    mainMenu()

#function to find the reciprocal
def findReciprocal():
    try:
        f=open(os.path.join(sys.path[0],"dataFile.txt"),"r")
        lines=f.readlines()
        for line in lines:
            l=line[0:(len(line)-1)]
            print("1/"+l+"=")
            try:
                print(1/int(l))
            except ValueError:
                print("Value Error occured")
            except ZeroDivisionError:
                print("Division by zero error")
            except:
                print("other error")
        f.close()
    

    except FileNotFoundError:
        print("dataFile.txt file doesnot found")
    input()
    mainMenu()

#function to find the average
def findSum():
    sum=0
    try:
        f=open(os.path.join(sys.path[0],"dataFile.txt"),"r")
        lines=f.readlines()
        for line in lines:
            l=line[0:(len(line)-1)]
            try:
                sum=sum+int(l)
            except:
                print("Type Error Occured while adding ",l)
        print("sum=",sum)
        f.close()

        
    except FileNotFoundError:
        print("dataFile.txt File doesnot exist")
    input()
    mainMenu()
    

#function for the main menu
def mainMenu():
    print("") #this print is for some space
    print("1.create file to store data")
    print("2.enter data in the file")
    print("3.view data")
    print("4.find the reciprocal of each data stored in file")
    print("5.find the sum of data stored in file")
    print("6.delete the file")
    print("7.Exit")
    print("")
    while True:
        try:
            choice=int(input("enter your choice:"))
        except ValueError:
            print("Value Error! Try again")
            continue
        if choice<8 and choice>0:
            break
    if choice==1:
        createFile()
    elif choice==2:
        enterData()
    elif choice==3:
        viewData()
    elif choice==4:
        findReciprocal()
    elif choice==5:
        findSum()
    elif choice==6:
        deleteFile()
    else:
        exit(0)


#program execution start from here
mainMenu()


