import threading 
from threading import*
import time
#'d' is the dictionary 
dic={} 

#for creating operation 
#we use syntax "create(key,value,timeout_value)"

def create(key,value,timeout=0):# timeout is optional you can continue by passing two arguments without timeout
    if key in dic:
        print("error: this key already exist in database") #error message for existing key[1]
    else:
        if(key.isalpha()):#constraint key is always a string
            #constraint for file size less than 1GB  
            #constraint for Jason object value less than 16KB 
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    record=[value,timeout]
                else:
                    record=[value,time.time()+timeout]
                if len(key)<=32: #constraints for key capped at 32chars
                    dic[key]=record
            else:
                print("Error!! Memory limit exceeded ")#error message[2]
        else:
            print("Error!! Invalid key entered... key must contain only alphabets and no special characters or numbers")#error message[3]

#for read operation
#we use syntax "read(key)"
            
def read(key):
    if key not in dic:
        print("Error!! given key does not exist in database. Please enter a valid key") #error message[4]
    else:
        temp=dic[key]
        if temp[1]!=0:
            if time.time()<temp[1]: #comparing the present time with expiry time
                strg=str(key)+":"+str(temp[0]) # returning the value in JasonObject format i.e..."key:value"
                return strg
            else:
                print("Error!! time-to-live of",key,"has expired") #error message[5]
        else:
            strg=str(key)+":"+str(temp[0])
            return strg

#for delete operation
#we use syntax "delete(key)"

def delete(key):
    if key not in dic:
        print("Error!! given key does not exist in database. Please enter a valid key") #error message[4]
    else:
        temp=dic[key]
        if temp[1]!=0:
            if time.time()<temp[1]: #comparing the current time with expiry time
                del dic[key]
                print("key successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message[5]
        else:
            del dic[key]
            print("key successfully deleted")

#operations during execution for create and read
create("Parvathi",31312)
create("chinni",1312)
print(read("Parvathi"),read("chinni"))

#operations during execution for delete and read
delete("Parvathi")
delete("chinni")
print(read("Parvathi"),read("chinni"))
