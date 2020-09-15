#Select Def
def prompt():
    if(whatdef == "writer"):
        writer()
    elif(whatdef == "reader"):
        reader()
    elif(whatdef == "delete"):
        delete()
    else:
        print("function not found\n")
        input("Press enter to exit...")

# Writer Part
def writer():
    f = open("wifireminder.txt", "a")
    name = input("What is your router name?\n\n")
    passw = input("\nWhat is your router password?\n\n")
    f.write(name)
    f.write(" : ")
    f.write(passw)
    f.write("\n")
    f.close
# Reader Part
def reader():
    f = open("wifireminder.txt", "r")
    print(f.read())
    input("\nPress enter to close...")
    f.close
# Delete Part
def delete():
    f = open("wifireminder.txt", "w")
    confirmation = input("Do you want to erase all data? Y/N\n")
    if confirmation == "Y" or confirmation == "y":
        f.write("")
        f.close
        input("Data erased...\nPress enter to exit")
    else:
        f.close

# Prompt Part
whatdef = input("What function you wanna use? (writer, reader, delete)\n")
prompt()