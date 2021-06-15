import os

def clearScreen():
    os.system('cls')

def reportSubMenu():
    print("Period Options:\n")
    print("1. Current Month Report")
    print("2. Data range report")
    print("3. Go back to previous options")
    print("4. logout")
    subMenuSelection = int(input("Please select a period option ( 1 to 4)"))
    return subMenuSelection

subMenuSelection = 0

def showMenu1():
    clearScreen()
    print("Report options:")
    print("1. Report per Customer")
    print("2. Report per Plan")
    print("3. General Top-up Report")
    print("4. Customers Report")
    print("5. Logout\n")

    selection = int(input("Please choose a report (1-5):"))
    return selection

selection = 0

while(selection != 5):
    selection = showMenu()
    clearScreen()
#    print(f"selection = {selection}")
    if(selection == 1):
        print("You selected Report per Customer!\n")
        reportSubMenu()
        input("Return to continue...")
    elif(selection == 2):
        print("You selected Option two!\n")
        input("Return to continue...")
    elif(selection == 3):
        print("You selected Option three!\n")
        input("Return to continue...")
    elif(selection == 4):
        print("You selected Option four!\n")
        input("Return to continue...")

print("Bye!")