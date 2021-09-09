from des import DesKey
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 12345)) #coonect to server
print(s.recv(1024).decode())
with open("key", "r") as f:
    des_key = f.read()

# keystr = "iamakeys" #key string must be multiple of 8
key = DesKey(des_key.encode('utf-8'))  # create key

while True:
    msg = input("type your message: ")
    ct = key.encrypt(msg.encode('utf-8'), padding=True) #encrypt a msg
    print("*"*18)
    print("key is ", des_key)
    print("sent plaintext is: %s"%msg)
    print("sent ciphertext is: %s"%ct.decode('utf-8', 'ignore'))
    print("*"*18)
    s.send(ct) #send ciphertext
    rcv = s.recv(1024) #recieved the msg
    print("*"*18)
    print("recieved ciphertext is: %s"%rcv.decode('utf-8', 'ignore'))
    pt = key.decrypt(rcv, padding=True).decode() #decrypt the msg
    print("recieved plaintext is: %s"%pt)
    print("*"*18)
    if pt == "bye": #if recieved msg is bye then break and close the connection
        break
s.close()