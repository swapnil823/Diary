#!/usr/bin/python
import sys
import os
import time
import datetime
from simplecrypt import encrypt, decrypt, DecryptionException
from getpass import getpass

today = str(datetime.date.today()).replace("-",'_')
timestamp =  str(datetime.datetime.now()).split(".")[0]
file_loc = os.path.abspath(os.path.dirname(__file__))

os.chdir(file_loc)
data_path = file_loc + "/DIARY_FILES"

if not os.path.exists(data_path):
    os.system("mkdir {}".format("DIARY_FILES"))
os.chdir(data_path)

passwd = getpass()
def createNew(fi):
    try:
        decAndSave(fi)
        with open('{}.txt'.format(fi), 'a') as df:
            df.write(timestamp)
            print("file exists ::: successfully decrypted")
    except DecryptionException as e:
        print("Invalid password")
        sys.exit()
    except:
        with open('{}.txt'.format(fi), 'a') as sf:
            sf.write(timestamp)
            print("created new file")

def openForEdit(fi):
    os.system("vim  '+normal Go' +startinsert "+'{}.txt'.format(fi))

def encAndSave(fi):
    with open('{}.txt'.format(fi), 'r') as sf, open('{}.enc'.format(fi), 'wb+') as df:
        df.write(encrypt(passwd, sf.read()))

def decAndSave(fi):
    with open('{}.txt'.format(fi), 'w') as df, open('{}.enc'.format(fi), 'rb') as sf:
        df.write(decrypt(passwd, sf.read()).decode())



if(len(sys.argv) > 1):
    decAndSave(sys.argv[1])
    f = sys.argv[1]
else:
    createNew(today)
    f = today

print("Decrypting File...{}".format(f))
openForEdit(f)
print("Encrypting File...{}".format(f))
encAndSave(f)
os.system("rm {}.txt".format(f))
