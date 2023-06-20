import os
from time import sleep 


# clear layer terlebih dahulu
os.system("clear")

# judulkan judul apk
title = """
===============================
A P L I K A S I - M Y  L O V E
===============================
"""

print(title)

# tunggu 3 detik
sleep(3)

username = input("Masukan username :")
address = input("Masukan address :")
phone = input("Masukan Phone :")
email = input("Masukan email :")
text = f"""
-------------------------------
    nama    : { username } 
-------------------------------
    alamat  : { address }
-------------------------------
    phone   : { phone }
-------------------------------
    email   : { email }
-------------------------------

"""

os.system("clear")
sleep(3)
print(text) 
os.system("reboot -y")
