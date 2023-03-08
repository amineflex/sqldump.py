import os
import pyfiglet
from pyfiglet import Figlet
from datetime import datetime


# Configuration
database_name = "INSERT_YOUR_DATABASE_NAME"
local_path = "dump/"
timestamp = datetime.now().strftime("%d-%m-%Y--%H:%M:%S")
filename = (f"{database_name}_{timestamp}.sql")


# Lancement
f = Figlet(font='slant')
print (f.renderText('SQLBackup'))
print ("© 2023 SQLBackup - by amineflex \n")

# MySQL dump
print (f"Copie de la base de donnée {database_name} dans le répertoire {local_path}")
try:
    os.system(f"mysqldump {database_name} > {filename} && mv {filename} {local_path}")
    print (f"✅ Ficher backup en local dans : {local_path}{filename}")

except:
    print (f"❌ Erreur : Impossible de backup la BDD {database_name}.")
    exit()

# 