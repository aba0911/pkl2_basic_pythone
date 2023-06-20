# menulis kan data kedalam file
 
#fileData = open("database.txt", "r" )

writeData = open("database.txt", "a")

text = input("Masukan text : ")

writeData.write(text + "\n")