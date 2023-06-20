import os

def listUndangan():
    fileData = open("database.txt", "a")
    nama = input("masukan nama : ")
    alamat = input("masukan alamat : ")
    phone = input ("masukan no phone : ")
    
    formatText = f"{nama}, {alamat}, {phone}\n"
    fileData.write(formatText)
    
def readUndangan():
    fileData = open ("database.txt", "r")
    result = fileData.read()
    os.system("clear")
    print(result)
    
listUndangan()
readUndangan()