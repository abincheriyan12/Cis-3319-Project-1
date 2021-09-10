# Abin Cheriyan
# Cis 3319 - Project 1
from des import DesKey
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 12345)) #coonect to server
print(s.recv(1024).decode())

with open("key", "r") as f:
    des_key = f.read()

#key string must be multiple of 8
key = DesKey(des_key.encode('utf-8'))  # create key

while True:
    msg = input(" Enter-the-message-you-want-to-encrypt/decrypt: ")
    ct = key.encrypt(msg.encode('utf-8'), padding = True) #encrypt a msg
    print("*" *20)
    print("key is ", des_key)
    print("sent plaintext is: %s" % msg)
    print("sent ciphertext is: %s" % ct.decode('utf-8', 'ignore'))
    print("*" *20)
    s.send(ct) #send ciphertext
    rcv = s.recv(1024) #recieved the msg
    print("*" *20)
    print(" Recieved ciphertext is: %s" % rcv.decode('utf-8', 'ignore'))
    pt = key.decrypt(rcv, padding = True).decode() #decrypt the msg
    print(" Recieved plaintext is: %s" % pt)
    print("*" *20)
    if pt == "bye": #if recieved msg is bye then break and close the connection
        print("Closing")
        break
s.close()